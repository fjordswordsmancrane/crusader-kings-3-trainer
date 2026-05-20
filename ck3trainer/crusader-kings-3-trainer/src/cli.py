"""
Command-line interface for the Crusader Kings III Trainer.
Provides a simple interactive menu.
"""

import logging
from .memory_reader import CK3MemoryReader
from .trainer_actions import CK3TrainerActions

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def main():
    """Main entry point for the trainer CLI."""
    print("Crusader Kings III Trainer")
    print("=" * 30)

    reader = CK3MemoryReader()
    if not reader.attach():
        print("Could not attach to CK3. Make sure the game is running.")
        return

    actions = CK3TrainerActions(reader)

    try:
        while True:
            print("\nOptions:")
            print("1. Show current gold")
            print("2. Set gold")
            print("3. Show current piety")
            print("4. Set piety")
            print("5. Show current prestige")
            print("6. Set prestige")
            print("7. Show current health")
            print("8. Set health")
            print("9. Exit")
            choice = input("Enter choice: ").strip()

            if choice == "1":
                gold = actions.get_gold()
                print(f"Current gold: {gold}")
            elif choice == "2":
                try:
                    val = int(input("Enter gold amount: "))
                    actions.set_gold(val)
                except ValueError:
                    print("Invalid number.")
            elif choice == "3":
                piety = actions.get_gold()  # placeholder, same offset for demo
                print(f"Current piety: {piety}")
            elif choice == "4":
                try:
                    val = int(input("Enter piety amount: "))
                    actions.set_piety(val)
                except ValueError:
                    print("Invalid number.")
            elif choice == "5":
                prestige = actions.get_gold()
                print(f"Current prestige: {prestige}")
            elif choice == "6":
                try:
                    val = int(input("Enter prestige amount: "))
                    actions.set_prestige(val)
                except ValueError:
                    print("Invalid number.")
            elif choice == "7":
                health = actions.get_health()
                print(f"Current health: {health}")
            elif choice == "8":
                try:
                    val = float(input("Enter health amount: "))
                    actions.set_health(val)
                except ValueError:
                    print("Invalid number.")
            elif choice == "9":
                print("Exiting...")
                break
            else:
                print("Invalid choice.")
    except KeyboardInterrupt:
        print("\nInterrupted.")
    finally:
        reader.detach()


if __name__ == "__main__":
    main()
