import random
from datetime import datetime as dt
import os

# Predefined bidding entities
bidding_entities = [
    {"name": "Entity_A", "id": "001"},
    {"name": "Entity_B", "id": "002"},
    {"name": "Entity_C", "id": "003"},
    {"name": "Entity_D", "id": "004"}
]

# Function to generate a single file
def generate_file(file_id, output_dir):
    file_name = f"grid_balancing_{file_id}.txt"
    date = dt.now().strftime("%Y%m%d")

    lines = []

    # Header
    lines.append(f"AAA|{date}|{file_id}|{file_name}|{dt.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # BBB (Load Balancing)
    for _ in range(1, 1000):
        grid_id = f"GRID_{random.randint(0,10)}"
        quantity = random.randint(-100, 100)
        lines.append(f"BBB|{grid_id}|{quantity}|{dt.now().timestamp()}")

        # CAA and associated bids
        total_accepted = 0
        num_entities = random.randint(3, 4)  # Ensure 3-4 entities are always selected
        for entity in bidding_entities[:num_entities]:
            lines.append(f"CAA|{grid_id}|{entity['name']}|{entity['id']}")

            bid_quantity = random.randint(1, max(1, abs(quantity) // 2))  # Ensure valid range
            bid_id = f"BID_{random.randint(1000, 9999)}"
            offer = random.randint(50, 150)  # Price in pence

            # Determine bid status
            if (
                (quantity > 0 and total_accepted + bid_quantity <= quantity) or
                (quantity < 0 and total_accepted + bid_quantity <= abs(quantity))
            ):
                status = "Accepted"
                total_accepted += bid_quantity
            else:
                status = "Declined"

            # CA1 (Bid Details)
            bid_time = dt.now().timestamp()
            lines.append(f"CA1|{grid_id}|{bid_quantity}|{bid_time}|{offer}")

            # CA2 (Bid Status)
            status_delay = random.randint(1, 10)
            lines.append(f"CA2|{bid_id}|{status}|{bid_time + status_delay}")

        # CBB (Difference)
        difference = quantity - total_accepted
        lines.append(f"CBB|{grid_id}|{quantity}|{difference}")

    # Footer
    lines.append(f"ZZZ|{date}|{file_name}|{dt.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Write to file
    with open(os.path.join(output_dir, file_name), "w") as f:
        f.write("\n".join(lines))

# Generate 10 files
def main():
    output_dir = f"{os.getcwd()}/output_files"
    os.makedirs(output_dir, exist_ok=True)

    for file_id in range(1, 2):
        generate_file(file_id, output_dir)

    print(f"Generated 10 files in {output_dir}")

if __name__ == "__main__":
    main()
