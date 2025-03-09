#!/usr/bin/env python3

"""Write a program to calculate the average scores of students from a CSV file"""

__author__ = "Lydia Frame"
__date__ = "03/09/2025"

import csv
import sys

FILENAME = "students.csv"  


def read_students(filename):
    """Reads student names and scores from a CSV file and returns a list."""
    try:
        students = []
        with open(filename, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                students.append(row)
        return students
    except FileNotFoundError as error:
        print(f"Could not find {filename}.")
        return []
    except Exception as error:
        print(type(error), error)
        return []


def calculate_averages(students):
    """Calculates and returns a list of (name, average) tuples."""
    averages = []
    for student in students:
        name = student[0]
        try:
            scores = [int(score) for score in student[1:]]  
            avg_score = round(sum(scores) / len(scores), 1)
            averages.append((name, avg_score))
        except ValueError:
            print(f"Invalid score found for {name}. Skipping.")
    return averages


def write_averages(filename, averages):
    """Writes the student averages to an output file."""
    try:
        with open(filename, "w") as file:
            for name, avg in averages:
                file.write(f"{name}: {avg}\n")
                print(f"{name}: {avg}") 
    except Exception as error:
        print(type(error), error)
        exit_program()


def exit_program():
    """Exits the program with a message."""
    print("Terminating program.")
    sys.exit()


def main():
    """Main function to run the program."""
    input_file = input("Input file? ") 
    print() 
    output_file = input("Output file? ")
    print()  

    students = read_students(input_file)
    if not students:  
        exit_program()
        
    averages = calculate_averages(students)
    write_averages(output_file, averages)


if __name__ == "__main__":
    main()
