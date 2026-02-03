from pipeline import generate_answer

print("\n" + "=" * 70)
print("✅ Sanskrit Document Retrieval-Augmented Generation System")
print("✅ CPU-only Inference Enabled")
print("=" * 70)

while True:
    query = input("\nEnter Sanskrit Query (or type 'exit'): ")

    if query.lower() == "exit":
        print("\n✅ System Closed Successfully.")
        break

    chunks, answer = generate_answer(query)

    print("\n" + "-" * 70)
    print("User Query:", query)

    print("\nTop Retrieved Context Chunks:")
    print("-" * 70)

    for i, chunk in enumerate(chunks):
        print(f"[{i+1}] {chunk}\n")

    print("Generated Answer:")
    print("-" * 70)
    print(answer)

    print("-" * 70)
