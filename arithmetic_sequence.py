def generate_arithmetic_sequence(n):
    if n <= 0:
        return []
    
    sequence = [2]  
    for i in range(1, n):
        next_term = sequence[-1] + 3
        sequence.append(next_term)
    
    return sequence

def main():
    try:
        n = int(input("Enter the number of terms (N): "))
        if n <= 0:
            print("Please enter a positive integer.")
            return
        
        result = generate_arithmetic_sequence(n)
        print("Output:", ",".join(map(str, result)))
    
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

if __name__ == "__main__":
    main()