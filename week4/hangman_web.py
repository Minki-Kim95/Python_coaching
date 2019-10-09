#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-
import random
import pymysql
from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)

HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def loadWordList():
    # words = []
    # try:
    #     conn = pymysql.connect(host='localhost',
    #                    user='root', password='1234',
    #                    db='words', charset='utf8')    # 없어질 디비이기에 보안유지 X
    #     curs = conn.cursor()
    #     sql = "select name from words.word"
    #     curs.execute(sql)
    #     rows = curs.fetchall()
    #     for row in rows:
    #         words.append(row[0])
    #     conn.close()
    # except Exception as e:
    #     print("Can't read from the word table")
    #     words = ['abcd', 'abcd']
    words = ['abcd', 'abcd']
    return words

def getRandomWord(wordList):
    # This function returns a random string from the passed list of strings.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    html = HANGMANPICS[len(missedLetters)]
    html += "\n"
    html += "Missed letters:"
    for letter in missedLetters:
        html += letter
    html += "\n"

    blanks = ''
    for i in range(len(secretWord)): # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks += secretWord[i]
        else:
            blanks += '_'

    for letter in blanks: # show the secret word with spaces in between each letter
        html += letter + " "
    html += "\n"

    return "<h3><pre>" + html + "</pre></h3>"

def check_Input(alreadyGuessed, guess):
    # Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
    success = 0

    if len(guess) != 1:
        html = '<font color=tomato size=4> Please enter a single letter. </font>'
    elif guess in alreadyGuessed:
        html = '<font color=tomato size=4>You have already guessed that letter. Choose again.</font>'
    elif guess not in 'abcdefghijklmnopqrstuvwxyz':
        html = '<font color=tomato size=4>Please enter a Alphabet</font>.'
    else:
        success = 1
        html = 'Guess a letter.'

    return success, html

# Check if the player has won
def checkCorrectAnswer(correctLetters, secretWord):
    foundAllLetters = True
    for i in range(len(secretWord)):
        if secretWord[i] not in correctLetters:
            foundAllLetters = False
            break
    return foundAllLetters

# Check if player has guessed too many times and lost
def checkWrongAnswer(missedLetters, secretWord):
    # Check if player has guessed too many times and lost
    if len(missedLetters) == len(HANGMANPICS) - 1:
        return True
    return False

@app.route("/")
def main():
    session["words"] = loadWordList()

    """Main application entry point."""
    header = '<h1>H A N G M A N</h1><p>'

    # input char
    inputform = 'Guess a letter.'
    inputform += '<form method = "post">'
    inputform += '<p>input: <input type = "text" name = "letter"></p>'
    inputform += '<input type = "submit" value = "input">'
    inputform += '</form>'

    session["missedLetters"] = ''
    session["correctLetters"] = ''
    session["gameSucceeded"] = False
    session["gameFailed"] = False
    session["secretWord"] = getRandomWord(session["words"])

    html = "<center>" + header + displayBoard(HANGMANPICS, session["missedLetters"], session["correctLetters"], session["secretWord"]) + inputform + "</center>"

    return html

@app.route("/", methods=['POST'])
def main_post():
    guess = request.form['letter']

    header = '<h1>H A N G M A N</h1><p>'

    # reaction of input
    inputvalid, message_input = check_Input(session["missedLetters"] + session["correctLetters"], guess)

    # input form
    inputform = message_input
    inputform += '<form method = "post">'
    inputform += '<p>input: <input type = "text" name = "letter"></p>'
    inputform += '<input type = "submit" value = "input">'
    inputform += '</form>'

    # when input value has problem
    if inputvalid == 0:
        html = "<center>" + header + displayBoard(HANGMANPICS, session["missedLetters"], session["correctLetters"],
                                                  session["secretWord"]) + inputform
    # when input value is valid
    else:
        if guess in session["secretWord"]:
            session["correctLetters"] += guess
            session["gameSucceeded"] = checkCorrectAnswer(session["correctLetters"], session["secretWord"])
        else:
            session["missedLetters"] += guess
            session["gameFailed"] = checkWrongAnswer(session["missedLetters"], session["secretWord"])

        # basic display form
        html = "<center>" + header + displayBoard(HANGMANPICS, session["missedLetters"], session["correctLetters"],
                                                  session["secretWord"])

        # when game is finish
        if session["gameSucceeded"] or session["gameFailed"]:
            if session["gameSucceeded"]:
                html += 'Yes! The secret word is "' + session["secretWord"] + '"! You have won!'
            else:
                html += 'You have run out of guesses!<p>After ' + str(
                    len(session["missedLetters"])) + ' missed guesses and ' + str(
                    len(session["correctLetters"])) + ' correct guesses, the word was "' + session["secretWord"] + '"'

            html += '<p>Do you want to play again? (yes or no)</p>'
            html += '<form method = "post">'
            html += '<p>input: <input type = "text" name = "again"></p>'
            html += '<input type = "submit" value = "input">'
            html += '</form>'

        # no success or fail
        else:
            html += inputform

    # if game
    html += "</center>"
    return html

if __name__ == "__main__":
    app.secret_key = "skku_python_study"
    app.run(host='0.0.0.0', port=80)
