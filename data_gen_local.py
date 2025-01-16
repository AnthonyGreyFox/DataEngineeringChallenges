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
    file_name = f"file_{file_id}.txt"
    date = dt.now().strftime("%Y%m%d")

    lines = []

    # Header
    lines.append(f"AAA|{date}|{file_id}|{file_name}|{dt.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # BBB (Load Balancing)
    for grid_id in range(1, 11):
        quantity = random.randint(-100, 100)
        lines.append(f"BBB|BalancingRequestOpened|{grid_id}|{quantity}|{dt.now().timestamp()}")

        # CAA and associated bids
        total_accepted = 0
        num_entities = random.randint(3, 4)  # Ensure 3-4 entities are always selected
        for entity in bidding_entities[:num_entities]:
            lines.append(f"CAA|bidder|{grid_id}|{entity['name']}|{entity['id']}")

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
            lines.append(f"CA1|bid_details|{grid_id}|{bid_quantity}|{bid_time}|{offer}")

            # CA2 (Bid Status)
            status_delay = random.randint(1, 10)
            lines.append(f"CA2|bid_status|{bid_id}|{status}|{bid_time + status_delay}")

        # CBB (Difference)
        difference = quantity - total_accepted
        lines.append(f"CBB|BalancingRequestClosed|{grid_id}|{quantity}|{difference}")

    # Footer
    lines.append(f"ZZZ|{date}|{file_name}|{dt.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Write to file
    with open(os.path.join(output_dir, file_name), "w") as f:
        f.write("\n".jo in(lines))

# Generate 10 files
def main():
    output_dir = "output_files"
    os.makedirs(output_dir, exist_ok=True)

    for file_id in range(1, 30):
        generate_file(file_id, output_dir)

    print(f"Generated 10 files in {output_dir}")

if __name__ == "__main__":
    main()
