from langgraph.graph import StateGraph, START , END
from typing import TypedDict

#define state model
class BMIState(TypedDict):
    weight: float
    height: float
    bmi: float


#define state graph
graph = StateGraph(BMIState)

def calculate_bmi(state: BMIState) -> BMIState:
    # state['bmi'] = state['weight'] / (state['height'] ** 2)
    # return state
    weight = state['weight']
    height = state['height']

    bmi = weight/(height**2)

    state['bmi'] = round(bmi, 2)

    return state


#add nodes to graph
graph.add_node('calculate_bmi', calculate_bmi, description="Start of the workflow")

#add edges to start
graph.add_edge(START, 'calculate_bmi')
graph.add_edge('calculate_bmi', END)

#compiple graph

workflow =graph.compile()

#execute graph
initial_state = {'weight': 70, 'height': 1.75}
output_state = workflow.invoke(initial_state)
print(output_state)


# #visualize graph
from Ipython.display import Image
Image(workflow.get_graph().draw_mermaind_png())
# #save graph
# graph.save("basic_workflow.json")