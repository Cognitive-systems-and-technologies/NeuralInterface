# Представления. Формирование шаблонов и данных для серверного рендеринга
import requests
import json
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
# Представления из модели
from .models import AgentsView, AgentGroupsView, AgentTypesView, AgentErrorsView, AgentFilesView, \
    AgentNeuralNetworkStateView
# Таблицы из модели
from .models import Agents, AgentGroups, AgentTypes, AgentErrors, AgentFiles, AgentNeuralNetworkState, NeuralAlgorithms
# Сериализаторы
from .serializers import GraphSerializer, AgentAddSerializer, SyncAgentDataSerializer, AgentDeleteSerializer, \
    AgentEditSerializer, GroupAddSerializer, GroupSerializer, NeuralAlgorithmsSerializer, AgentErrorsSerializer


# Формирование данных для веб-страниц и рендер шаблона
# Формирование шаблона и данных для серверного рендеринга базовой страницы
def index(request):
    template = loader.get_template('interface/index.html')
    agents = AgentsView.objects.all()
    agentGroups = AgentGroupsView.objects.all()
    agentTypes = AgentTypesView.objects.all()
    agentFiles = AgentFilesView.objects.all()
    agentNeuralNetworkState = AgentNeuralNetworkStateView.objects.all()
    neuralAlgorithms = NeuralAlgorithms.objects.all()
    array = {'agents': agents,
             'agentGroups': agentGroups,
             'agentTypes': agentTypes,
             'agentFiles': agentFiles,
             'agentNeuralNetworkState': agentNeuralNetworkState,
             'neuralAlgorithms': neuralAlgorithms}
    return HttpResponse(template.render(array, request))


# Формирование шаблона и данных для серверного рендеринга страницы с графиком
def monitor(request):
    template = loader.get_template('interface/monitor.html')
    agents = AgentsView.objects.all()
    agentErrors = AgentErrorsView.objects.all()
    array = {'agents': agents,
             'agentErrors': agentErrors}
    return HttpResponse(template.render(array, request))


# Формирование шаблона и данных для серверного рендеринга страницы с информацией
def info(request):
    template = loader.get_template('interface/info.html')
    agents = AgentsView.objects.all()
    array = {'agents': agents}
    return HttpResponse(template.render(array, request))


# Управление агентами
# Добавление нового агента
class AgentAddData(generics.ListAPIView):
    def post(self, request):
        # Создание экземпляра сериализатора с полученными данными запроса
        serializer = AgentAddSerializer(data=request.data)

        # Проверка валидности данных сериализатора
        if serializer.is_valid():
            # Извлечение необходимых данных из запроса
            agent_group_id = request.data.get('agent_group_id')
            agent_type_id = request.data.get('agent_type_id')
            agent_mac_address = request.data.get('agent_mac_address')

            # Проверка наличия агента с указанным MAC-адресом в базе данных
            agent_mac_address_check = Agents.objects.filter(agent_mac_address=agent_mac_address).exists()

            if agent_mac_address_check:
                # Если агент с указанным MAC-адресом уже существует, возвращается сообщение об ошибке
                message = "Агент с таким MAC адрессм уже существует"
                return Response(message, status=status.HTTP_200_OK)

            try:
                # Получение группы агента по указанному agent_group_id
                agent_group = AgentGroups.objects.get(id=agent_group_id)
            except AgentGroups.DoesNotExist:
                # Если указанный agent_group_id не существует, возвращается сообщение об ошибке
                return Response({"agent_group_id": "Invalid agent group ID"}, status=400)

            try:
                # Получение типа агента по указанному agent_type_id
                agent_type = AgentTypes.objects.get(id=agent_type_id)
            except AgentTypes.DoesNotExist:
                # Если указанный agent_type_id не существует, возвращается сообщение об ошибке
                return Response({"agent_type_id": "Invalid agent type ID"}, status=400)

            try:
                # Проверка существования агента по указанному agent_type_id
                agent_mac_address_check = Agents.objects.get(id=agent_type_id)
            except AgentTypes.DoesNotExist:
                # Если указанный agent_type_id не существует, возвращается сообщение об ошибке
                return Response({"agent_type_id": "Invalid agent type ID"}, status=400)

            # Назначение связанных объектов в данных сериализатора
            serializer.validated_data['agent_group'] = agent_group
            serializer.validated_data['agent_type'] = agent_type

            # Сохранение сериализатора
            serializer.save()

            # Возвращение успешного ответа
            return Response("Агент успешно добавлен", status=status.HTTP_200_OK)

        # Если данные сериализатора невалидны, возвращается сообщение об ошибке
        return Response(serializer.errors, status=400)


# Изменение данных агента
class AgentEditData(generics.UpdateAPIView):
    queryset = Agents.objects.all()
    serializer_class = AgentEditSerializer

    def update(self, request, *args, **kwargs):
        global agent_another
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            # Получение данных из запроса
            agent_group_id = request.data.get('agent_group_id')
            agent_type_id = request.data.get('agent_type_id')
            agent_mac_address_query = request.data.get('agent_mac_address')

            # Получение ID агента
            agent_id = instance.id

            # Получение данных из БД по ID агента
            agent_current = Agents.objects.get(id=agent_id)

            try:
                # Попытка получить данные из БД по MAC-адресу
                agent_another = Agents.objects.get(agent_mac_address=agent_mac_address_query)

                # Если ID агента, полученного из БД по ID агента (текущий агент),
                # не совпадает с ID агента, полученного из БД по MAC-адресу
                # (другой агент с таким же MAC-адресом), выводится соответствующее сообщение
                if agent_current.id != agent_another.id:
                    message = "Агент с таким MAC адресом уже существует"
                    return Response(message, status=status.HTTP_200_OK)

            except Agents.DoesNotExist:
                # Если данных нет, код продолжает выполняться
                pass

            try:
                agent_group = AgentGroups.objects.get(id=agent_group_id)
            except AgentGroups.DoesNotExist:
                return Response({"agent_group_id": "Invalid agent group ID"}, status=400)

            try:
                agent_type = AgentTypes.objects.get(id=agent_type_id)
            except AgentTypes.DoesNotExist:
                return Response({"agent_type_id": "Invalid agent type ID"}, status=400)

            # Присваивание связанных объектов данным сериализатора
            serializer.validated_data['agent_group'] = agent_group
            serializer.validated_data['agent_type'] = agent_type

            self.perform_update(serializer)
            return Response("Агент успешно изменен", status.HTTP_200_OK)

        return Response(serializer.errors, status=400)


# Удаление агента
class AgentDeleteData(generics.DestroyAPIView):
    queryset = Agents.objects.all()
    serializer_class = AgentDeleteSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        agent_id = instance.id

        # Проверка наличия связанных записей агента в различных таблицах
        errors_exist = AgentErrors.objects.filter(agent_id=agent_id).exists()
        neural_state_exist = AgentNeuralNetworkState.objects.filter(agent_id=agent_id).exists()
        errors_file_exist = AgentFiles.objects.filter(agent_id=agent_id).exists()

        if errors_file_exist:
            # Если связанные записи существуют в таблице файлов агентов,
            # возвращается сообщение об ошибке
            message = "Запись с привязкой данного агента существует в таблице файлов агентов"
        elif errors_exist:
            # Если связанные записи существуют в таблице обучения агентов,
            # возвращается сообщение об ошибке
            message = "Запись с привязкой данного агента существует в таблице обучения агентов"
        elif neural_state_exist:
            # Если связанные записи существуют в таблице состояний нейросети,
            # возвращается сообщение об ошибке
            message = "Запись с привязкой данного агента существует в таблице состояний нейросети"
        else:
            # Если связанные записи отсутствуют, производится удаление записи агента
            message = 'Агент успешно удален'
            instance.delete()
            return Response(message, status=status.HTTP_200_OK)

        return Response(message, status=status.HTTP_200_OK)


# Классы для страницы index.js
# Управление группами агентов
# Добавление группы агентов
class GroupAddData(generics.ListAPIView):
    def post(self, request):
        # Создание экземпляра сериализатора с полученными данными запроса
        serializer = GroupAddSerializer(data=request.data)

        # Проверка валидности данных сериализатора
        if serializer.is_valid():
            # Сохранение сериализатора
            serializer.save()
            # Возвращение данных сериализатора вместе с успешным статусом
            return Response(serializer.data, status=201)

        # Если данные сериализатора невалидны, возвращается сообщение об ошибке
        return Response(serializer.errors, status=400)


# Изменение группы агентов
class GroupEditData(generics.UpdateAPIView):
    queryset = AgentGroups.objects.all()
    serializer_class = GroupSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            # Обновление данных сериализатора
            self.perform_update(serializer)
            # Возвращение обновленных данных сериализатора
            return Response(serializer.data)

        # Если данные сериализатора невалидны, возвращается сообщение об ошибке
        return Response(serializer.errors, status=400)


# Удаление группы агентов
class GroupDeleteData(generics.DestroyAPIView):
    queryset = AgentGroups.objects.all()
    serializer_class = GroupSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        group_id = instance.id

        # Проверка наличия связанных записей группы в таблице агентов
        group_exist = Agents.objects.filter(agent_group_id=group_id).exists()

        if group_exist:
            # Если связанные записи существуют в таблице агентов,
            # возвращается сообщение об ошибке
            message = "Запись с привязкой данной группы существует в таблице агентов"
        else:
            # Если связанные записи отсутствуют, производится удаление записи группы агентов
            message = "Группа успешно удалена"
            instance.delete()
            return Response(message, status=status.HTTP_200_OK)

        return Response(message, status=status.HTTP_200_OK)


# Классы для страницы index.js
# Данные для получения данных графика для определенного агента
class GraphApiData(generics.ListAPIView):
    serializer_class = GraphSerializer

    def get_queryset(self):
        agent_id = self.request.query_params.get('agent_id')

        if agent_id is None:
            # Если параметр agent_id отсутствует, возвращается сообщение об ошибке
            return Response("agent_id parameter is required.", status=400)

        # Фильтрация записей AgentErrorsView по agent_id
        return AgentErrorsView.objects.filter(agent_id=agent_id)


# Удаление данных определенного агента из таблицы обучения агентов
class AgentErrorsDeleteData(APIView):
    def delete(self, request, agent_id):
        try:
            # Удаление данных об ошибках агента с помощью фильтрации по agent_id
            deleted_data = AgentErrors.objects.filter(agent_id=agent_id).delete()

            # Создание сериализатора с удаленными данными
            serializer = AgentErrorsSerializer(deleted_data, many=True)

            # Возвращение сообщения об успешном удалении
            return Response("Данные успешно удалены", status=status.HTTP_200_OK)
        except Exception as e:
            # Возвращение сообщения об ошибке при возникновении исключения
            return Response("Error: " + str(e), status=200)


# Синхронизация данных между агентом и базой данных сервера
class SyncAgentData(generics.ListAPIView):
    def post(self, request):
        mes_data = request.data

        if mes_data['m'] == 'authorization':
            # Получение данных агента из запроса
            agent_data = mes_data['b']
            agent_name = agent_data['name']
            agent_ip_address = request.META.get('REMOTE_ADDR')
            agent_mac_address = agent_data['mac']
            agent_port = agent_data['port']

            # Подготовка данных для добавления или обновления записи агента
            agent_data_add = {
                'agent_name': agent_name,
                'agent_mac_address': agent_mac_address,
                'agent_ip_address': agent_ip_address,
                'agent_port': agent_port,
                'agent_status': '1',
                'datetime_change': datetime.now(),
                'datetime_create': datetime.now()
            }

            # Создание сериализатора с подготовленными данными агента
            serializer = SyncAgentDataSerializer(data=agent_data_add)

            if serializer.is_valid():
                try:
                    # Проверка существования записи агента по MAC адресу
                    agent = Agents.objects.get(agent_mac_address=agent_mac_address)
                    agent.agent_name = agent_name
                    agent.agent_ip_address = agent_ip_address
                    agent.agent_port = agent_port
                    agent.agent_status = 1
                    agent.datetime_change = datetime.now()
                    agent.save()
                except Agents.DoesNotExist:
                    # Создание новой записи агента
                    Agents.objects.create(
                        agent_name=agent_name,
                        agent_mac_address=agent_mac_address,
                        agent_ip_address=agent_ip_address,
                        agent_port=agent_port,
                        agent_status=1,
                        datetime_create=datetime.now()
                    )

                return Response({'message': 'Agent info saved/updated successfully.'})
            else:
                return Response(serializer.errors, status=400)


# Отправка запроса агенту
class SendRequestToAgent(generics.ListAPIView):
    def post(self, request):
        query_type = request.data.get('t')

        if query_type == 'command':
            # Если запрос с фронтенда, формируем запрос и отправляем данные на агента

            # Извлечение CSRF-токена из заголовков запроса
            csrf_token = request.META.get('CSRF_COOKIE', '')
            headers = {
                'X-CSRFToken': csrf_token  # Включение CSRF-токена в заголовки
            }

            agentId = request.data.get('agent_id')
            agentCommand = request.data.get('agent_command')
            agentData = Agents.objects.get(id=agentId)
            agentIpAddress = agentData.agent_ip_address
            agentPort = agentData.agent_port

            if agentIpAddress is None or agentPort is None or agentIpAddress == '' or agentPort == '':
                return Response("Проверьте данные IP-адреса и порта агента", status=400)
            elif agentCommand == 'download':
                t_value = 'request'
                # Обычный запрос на получение данных с агента и сохранение ответа в БД
            elif agentCommand == 'upload':
                t_value = 'request'
                # Вытянуть данные из таблицы и отправить на агента
            else:
                t_value = 'command'
                pass

            url = 'http://' + agentIpAddress + ':' + agentPort
            data = {
                'r': 'domain',
                't': t_value,
                'm': agentCommand,
                'b': ''
            }

            # Отправка HTTP-запроса с извлеченными данными
            try:
                response = requests.post(url, headers=headers, json=data)
                response.raise_for_status()
                # Обработка ответа здесь
                result = response.json()
                # Возврат успешного ответа
                return Response(result, status=status.HTTP_200_OK)
            except ConnectionError as e:
                # Обработка ошибки соединения
                message = 'Ошибка: Ошибка соединения - ' + str(e)
                return Response(message, status=status.HTTP_200_OK)
            except requests.exceptions.RequestException as e:
                # Обработка других исключений запроса
                message = 'Ошибка: ' + str(e)
                return Response(message, status=status.HTTP_200_OK)

        elif query_type == 'request':
            # Если запрос с агента, обрабатываем данные
            return Response('test', status=status.HTTP_200_OK)
        else:
            return Response('global error', status=status.HTTP_200_OK)


# Добавление данных в таблицу агента
class GraphAgentDataAdd(generics.ListAPIView):
    def post(self, request):
        mes_data = request.data
        if mes_data['m'] == 'loss':
            agent_data = mes_data['b']
            # Данные для тестирования
            # agent_data = '{"points":{"actor": [0,0.7345353,1,0.353553,2,0.12313123], "critik": [1,0.5345345345,2,0.446464645,3,0.1213123131], "acto": [0,0.8912,1,0.7689,2,0.56787578], "actor": [0,0.7345353,1,0.353553,2,0.12313123]}}'
            # data_conversion = json.loads(agent_data)
            # Получаем IP-адрес агента, откуда пришел запрос
            points = agent_data['points']
            agent_ip_address = request.META.get('REMOTE_ADDR')
            print(agent_ip_address)
            agents = Agents.objects.filter(agent_ip_address=agent_ip_address)
            if len(agents) == 0:
                # Агенты не найдены
                return Response({"Ошибка": "IP-адрес не существует в базе данных"}, status=400)
            elif len(agents) > 1:
                # Найдено несколько агентов
                return Response({"Ошибка": "В базе данных существует более одного значения с таким IP-адресом"},
                                status=400)
            # Получаем идентификатор агента
            agent_id = agents[0].id
            print('ID агента: ', agent_id)
            for key, values in points.items():
                # Запрос к таблице NeuralAlgorithms для каждого значения
                matching_records = NeuralAlgorithms.objects.filter(algorithm_code_name=key)
                print('Ключ: ', key, 'Значение: ', values)
                # Проверяем, найдены ли соответствующие записи
                algorithm_id = 0
                if matching_records:
                    algorithm_id = matching_records[0].id
                else:
                    # Создаем новую запись с извлеченным значением
                    if key:
                        data = {
                            'algorithm_code_name': key,
                            'datetime_create': datetime.now()
                        }
                        serializer = NeuralAlgorithmsSerializer(data=data)
                        if serializer.is_valid():
                            instance = serializer.save()
                            algorithm_id = instance.pk
                        else:
                            return Response({"Ошибка": "Ошибка записи нового алгоритма в базу данных"}, status=400)

                for i in range(0, len(values), 2):
                    agent_step = values[i] if i < len(values) else None
                    agent_error_value = values[i + 1] if i + 1 < len(values) else None

                    if agent_step is not None and agent_error_value is not None:
                        agent_error_data = {
                            'agent_step': agent_step,
                            'agent_error_value': agent_error_value,
                            'datetime_create': datetime.now(),
                            'agent_error_info': '',
                            'agent': agent_id,
                            'algorithm': algorithm_id
                        }
                        serializer = AgentErrorsSerializer(data=agent_error_data)
                        if serializer.is_valid():
                            serializer.save()
                        else:
                            return Response({"Ошибка": "Ошибка записи ошибки агента в базу данных"}, status=400)

            return Response({'Успех': 'Данные успешно занесены в базу данных'})
        else:
            return Response(status=400)
