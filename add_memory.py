from langgraph.checkpoint.memory import MemorySaver

from add_tools import graph_builder, png_bytes

memory = MemorySaver()

graph = graph_builder.compile(checkpointer=memory)

try:
    png_bytes = graph.get_graph().draw_mermaid_png()
    with open('graph.png', 'wb') as f:
        f.write(png_bytes)
except Exception as e:
    print(f"Could not generate graph image: {e}")