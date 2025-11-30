from agents.orchestrator import AgriLoopOrchestrator

def main():
    orchestrator = AgriLoopOrchestrator()

    result = orchestrator.run(
        input_data={
            "image_path": "examples/sample_waste.jpg",
            "location": "Chattogram, Bangladesh",
            "quantity_kg": 25
        }
    )

    print("\nFinal Result:\n")
    print(result)

if __name__ == "__main__":
    main()
