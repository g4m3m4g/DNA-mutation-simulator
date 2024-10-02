import streamlit as st
import random

# Function to simulate mutations in a DNA sequence
def mutate_dna(dna, mutation_type):
    mutated_dna = list(dna)
    mutation_details = []

    for i in range(len(mutated_dna)):
        if random.random() < 0.1:  # 10% chance of mutation
            if mutation_type == "Point Mutation":
                original_nucleotide = mutated_dna[i]
                mutated_dna[i] = random.choice(['A', 'T', 'C', 'G'])  # Point mutation
                mutation_details.append((i, original_nucleotide, mutated_dna[i]))

            elif mutation_type == "Insertion":
                insert_nucleotide = random.choice(['A', 'T', 'C', 'G'])
                mutated_dna.insert(i, insert_nucleotide)  # Insertion
                mutation_details.append((i, None, insert_nucleotide))  # Record insertion

            elif mutation_type == "Deletion":
                if mutated_dna:  # Ensure there's something to delete
                    original_nucleotide = mutated_dna[i]
                    del mutated_dna[i]  # Deletion
                    mutation_details.append((i, original_nucleotide, None))  # Record deletion
                # Adjust the loop to account for changes in length
                continue

    return ''.join(mutated_dna), mutation_details

# Function to highlight mutations
def highlight_changes(original, mutated, changes):
    highlighted = ""
    for i in range(len(original)):
        if i in [c[0] for c in changes]:  # Check if the index is a mutation
            change = changes[[c[0] for c in changes].index(i)]
            if change[1] is not None:  # Point mutation
                highlighted += f"<span style='color: red;'>{change[2]}</span>"  # Highlight mutated nucleotide
            else:  # Insertion
                highlighted += f"<span style='color: green;'>[{change[2]}]</span>"  # Highlight inserted nucleotide
        else:
            highlighted += original[i]  # Keep original nucleotide

    return highlighted

# Streamlit app
st.title("DNA Mutation Simulator")

# Input DNA sequence
user_input = st.text_area("Enter DNA sequence (A, T, C, G):", height=150)

# Mutation type selection
mutation_type = st.selectbox("Select Mutation Type:", ["Point Mutation", "Insertion", "Deletion"])

if st.button("Simulate Mutation"):
    if user_input:
        mutated_sequence, changes = mutate_dna(user_input, mutation_type)
        highlighted_sequence = highlight_changes(user_input, mutated_sequence, changes)
        
        st.subheader("Original DNA Sequence:")
        st.write(user_input)
        st.subheader("Mutated DNA Sequence:")
        st.write(mutated_sequence)
        st.subheader("Highlighted Changes in Sequence:")
        st.markdown(highlighted_sequence, unsafe_allow_html=True)  # Use HTML to highlight changes
    else:
        st.error("Please enter a valid DNA sequence.")
