import sys

def main():
    # Separate storage arrays to handle clean grouping
    pending_tasks = []
    completed_tasks = []

    while True:
        print("\n=== TASK MANAGER MENU ===")
        print("1. Enter Task Details")
        print("2. View Pending Tasks")
        print("3. View Completed Tasks")
        print("4. Update Task Status")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ").strip()

        if choice == '1':
            task_name = input("Enter the task name: ").strip()
            if task_name:
                pending_tasks.append(task_name)
                print(f"➕ Task '{task_name}' added to pending list.")
            else:
                print("❌ Task name cannot be empty.")

        elif choice == '2':
            print("\n--- ⏳ PENDING TASKS ---")
            if not pending_tasks:
                print("No pending tasks.")
            for i, task in enumerate(pending_tasks, 1):
                print(f"{i}. {task} [⏳ Pending]")

        elif choice == '3':
            print("\n--- ✅ COMPLETED TASKS ---")
            if not completed_tasks:
                print("No completed tasks yet.")
            for i, task in enumerate(completed_tasks, 1):
                print(f"{i}. {task} [✅ Completed]")

        elif choice == '4':
            print("\n--- ⏳ PENDING TASKS ---")
            if not pending_tasks:
                print("No pending tasks available to update.")
                continue
                
            for i, task in enumerate(pending_tasks, 1):
                print(f"{i}. {task}")
                
            try:
                idx_input = input("\nMention the task number to update: ").strip()
                idx = int(idx_input) - 1
                
                if 0 <= idx < len(pending_tasks):
                    confirm = input(f"Move '{pending_tasks[idx]}' to completed? select yes(y), no(n): ").strip().lower()
                    if confirm == 'y':
                        completed_task = pending_tasks.pop(idx)
                        completed_tasks.append(completed_task)
                        print("✨ Task status updated successfully!")
                        
                        # Re-display pending tasks immediately to show updates
                        print("\n--- Updated Pending Tasks ---")
                        if not pending_tasks:
                            print("No pending tasks remaining.")
                        for i, task in enumerate(pending_tasks, 1):
                            print(f"{i}. {task} [⏳ Pending]")
                    else:
                        print("Update cancelled. Task remains pending.")
                else:
                    print("❌ Invalid task number selection.")
            except ValueError:
                print("❌ Please enter a valid numerical serial number.")

        elif choice == '5':
            print("🚪 Exiting application. Goodbye!")
            sys.exit()

        else:
            print("❌ Invalid choice. Please pick a number from 1 to 5.")

if __name__ == "__main__":
    main()