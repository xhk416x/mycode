#!/usr/bin/env python3
"""Rock Paper Scissors Game | by Wes Pritchard"""
import random

def main():
    """body of the game"""
    
    choice= input("Rock, Paper, Scissors?\n>")
    choice= choice.lower()
    
    if choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice (Do you suck at spelling?)")
        exit()

    botoptions= ["rock", "paper", "scissors"]    
    botchoice= random.choice(botoptions)

    print(f"You picked {choice}.")
    print(f"I picked {botchoice}.")

    if choice == "scissors" and botchoice == "paper":
        print("You Win!")
    elif choice == "rock" and botchoice == "scissors":
        print("You Win!")
    elif choice == "paper" and botchoice == "rock":
        print("You Win!")
    elif choice == "paper" and botchoice == "scissors":
        print("You Lose!")
    elif choice == "scissors" and botchoice == "rock":
        print("You Lose!")
    elif choice == "rock" and botchoice == "paper":
        print("You Lose!")
    else:
        print("It's a TIE!")

main()