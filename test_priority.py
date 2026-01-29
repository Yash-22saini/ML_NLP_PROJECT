from src.priority_logic import assign_priority, recommend_action

priority = assign_priority("negative", "payment")
action = recommend_action(priority)

print(priority)
print(action)
