# Stock-Simulator
A stock simulation program that allows you to buy and sell stock at the following companies: Microsoft, Apple, Tesla, Facebook, Nvidia, Disney, Paypal.  
# All money and stock in the program is NOT real, this program is merely meant as a "What if."

All stock prices are gathered at runtime and every minute from Yahoo Finance. **These are the real prices of the stocks.** 

The user's data is saved in a file called *data.json*, **which is created if the program is ran without it**. This gives you $1000 of startup cash to use, however you could change the value in the json file if you want more money.  

A default data.json file is provided.

The json file stores current money, the amount of each stock held, and the price it was purchased at (To track profit).  

# Notes
This program is a work in progress and is in very early stages. There are bound to be bugs/edge-cases I haven't accounted for.

# Planned Features
- GUI
- More companies
- Choose how much money to start with
- See price changes from certain time intervals (%s)
- Option to reset file
- Bug fixes and more documentation
