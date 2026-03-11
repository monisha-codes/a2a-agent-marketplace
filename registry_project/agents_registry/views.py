from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Agent
from .serializers import AgentSerializer


@api_view(["POST"])
def register_agent(request):
    serializer = AgentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Agent registered"})
    return Response(serializer.errors)


@api_view(["GET"])
def list_agents(request):
    agents = Agent.objects.all()
    serializer = AgentSerializer(agents, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def search_agents(request):
    capability = request.GET.get("capability")

    agents = Agent.objects.all()
    result = []

    for agent in agents:
        if capability in agent.capabilities:
            result.append(agent)

    serializer = AgentSerializer(result, many=True)
    return Response(serializer.data)
