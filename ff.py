from collections import defaultdict

def compute_first(grammar):
    first = defaultdict(set)

    def first_of(symbol):
        # If terminal, return itself
        if not symbol.isupper():
            return {symbol}
        
        # If already computed, return
        if symbol in first and len(first[symbol]) > 0:
            return first[symbol]
        
        # Compute FIRST for each production of this non-terminal
        for production in grammar[symbol]:
            for char in production:
                char_first = first_of(char)
                first[symbol].update(char_first - {'ε'})
                
                # If epsilon is not in first of this char, break
                if 'ε' not in char_first:
                    break
            else:
                first[symbol].add('ε')
        return first[symbol]

    for non_terminal in grammar:
        first_of(non_terminal)

    return first

# Function to compute FOLLOW set
def compute_follow(grammar, first):
    follow = defaultdict(set)
    start_symbol = next(iter(grammar))  # Start symbol is the first one defined in the grammar
    follow[start_symbol].add('$')  # Add end marker to start symbol's FOLLOW set

    def follow_of(symbol):
        for lhs, productions in grammar.items():
            for production in productions:
                if symbol in production:
                    pos = production.index(symbol)
                    while pos < len(production) - 1:
                        next_symbol = production[pos + 1]
                        follow[symbol].update(first[next_symbol] - {'ε'})
                        if 'ε' not in first[next_symbol]:
                            break
                        pos += 1
                    else:
                        if lhs != symbol:
                            follow[symbol].update(follow_of(lhs))
        return follow[symbol]

    for non_terminal in grammar:
        follow_of(non_terminal)

    return follow

# Helper function to add productions to the grammar
def add_production(grammar, non_terminal, production):
    grammar[non_terminal].append(production.split())

# Example usage
if __name__ == "__main__":
    grammar = defaultdict(list)

    # Example Grammar: 
    # S -> AB
    # A -> a | ε
    # B -> b

    add_production(grammar, 'S', 'A B')
    add_production(grammar, 'A', 'a')
    add_production(grammar, 'A', 'ε')
    add_production(grammar, 'B', 'b')

    # Compute FIRST and FOLLOW sets
    first = compute_first(grammar)
    follow = compute_follow(grammar, first)

    print("FIRST sets:")
    print(first)
    for non_terminal, f_set in first.items():
        print(f"FIRST({non_terminal}) = {{", ', '.join(f_set), "}}")

    print("\nFOLLOW sets:")
    for non_terminal, f_set in follow.items():
        print(f"FOLLOW({non_terminal}) = {{", ', '.join(f_set), "}}")
