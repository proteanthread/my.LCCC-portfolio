import random

def convert_to_all_bases(input_type, value):

    # This program converts a single value in one base to all four bases.
    
    #   Choice  "B" (Binary),
    #           "H" (Hex),
    #           "O" (Octal),
    #           "D" (Decimal)

    # Returns:
    #   Keys are base names, values are representations in that base.
        
    # Raises:
    #    an Error: If value is invalid for the chosen base.

    base_map = {"B": 2, "H": 16, "O": 8, "D": 10}
    
    # Convert input to decimal
    decimal_value = int(value, base_map[input_type])
    
    # Convert from decimal to all bases
    return {
        "Binary": bin(decimal_value)[2:],
        "Hexadecimal": hex(decimal_value)[2:].upper(),
        "Octal": oct(decimal_value)[2:],
        "Decimal": str(decimal_value)
    }


def main():
    type_mapping = {
        "B": "Binary",
        "H": "Hexadecimal",
        "O": "Octal",
        "D": "Decimal"
    }
    
    while True:
        # Get input type
        print("\nSelect input type:")
        print("  B. Binary")
        print("  H. Hexadecimal")
        print("  O. Octal")
        print("  D. Decimal")
        
        input_type = input("Enter your choice: ").strip()
        
        if input_type not in type_mapping:
            print("? Invalid choice! Please select B, H, O, or D.")
            continue
        
        # Get input value
        input_value = input("Enter the value: ").strip()
        
        if not input_value:
            print("? Value cannot be empty!")
            continue
        
        # Try conversion
        try:
            conversions = convert_to_all_bases(input_type, input_value)
        except ValueError:
            print(f"? Invalid {type_mapping[input_type]} value!")
            continue
        
        # Build output order: shuffle other bases, then append input base last
        input_type_name = type_mapping[input_type]
        other_bases = [b for b in conversions.keys() if b != input_type_name]
        random.shuffle(other_bases)
        output_order = other_bases + [input_type_name]
        
        # Display results
        print(f"\n? Input: {input_type_name} - {input_value}")
        print("\n\tConversions:")
        print("-" * 45)
        for i, base in enumerate(output_order, 1):
            print(f"  {i}. {base:15s} {conversions[base]}")
        
        # Ask if user wants another conversion
        again = input("\nConvert another value? (y/n): ").strip().lower()
        if again != 'y':
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
