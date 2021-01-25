#!/usr/bin/python3


import requests
import json
import os
import datetime
from bs4 import BeautifulSoup

def main():

    obj = {}

    url = "https://cathiesark.com/ark-funds-combined/complete-holdings"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    for script in soup.find_all("script"):
        try:
            obj = json.loads(script.string)
            if "props" in obj.keys():
                break
        except Exception:
            pass

    return_value = print_ark_report(obj)

    
# end main()

def print_ark_trades(obj):
    # Ark Trades
    for trade in obj["props"]["pageProps"]["arkTrades"]:
        print(trade)
        output = "{:<8} {:<12} {:<12} {:<5}".format(trade["ticker"], trade["date"], trade["direction"], trade["fund"])
        print( output)

# end print_ark_trades(obj):

def print_ark_report(obj):
    report_obj = {}

    for trade in obj["props"]["pageProps"]["arkTrades"]:
        
        if trade["date"] not in report_obj.keys():
            report_obj[ trade["date"] ] = {}
        if trade["ticker"] not in report_obj[ trade["date"] ].keys():
            report_obj[ trade["date"] ][ trade["ticker"] ] = []
        
        report_obj[ trade["date"] ][ trade["ticker"] ].append(trade)

    html = return_html_text_ark_trades( report_obj )
    open(os.environ["ARK_TRADES_REPORT"], "w").write(html)
        # output = "{:<8} {:<12} {:<12} {:<5}".format(trade["ticker"], trade["date"], trade["direction"], trade["fund"])
        # print( output)

# end print_ark_trades(obj):

def return_html_text_ark_trades( report_obj ):

    report_obj = keep_recent_days( report_obj, 20 )
    uniq_tickers = []
    uniq_dates = []
    for date in report_obj.keys():
        if date not in uniq_dates:
            uniq_dates.append(date)
        for ticker in report_obj[date].keys():
            if ticker not in uniq_tickers:
                uniq_tickers.append(ticker)

    html = ""
    html = html + """
<html>
  <head>
    <title>Ark historical trades</title>
  </head>
  <body>
  <table border=1>
"""

    html = html + get_head_row(uniq_dates)
    for ticker in uniq_tickers:
        html = html + get_ticker_row(report_obj, uniq_dates, ticker)
        pass


    html = html + """
    </table>
  </body>
</html>
"""
    
    return html

# end return_html_text_ark_trades( report_obj )

def keep_recent_days( report_obj, days ):

    return_obj = {}
    if days == 0:
        return report_obj
    else:
        for date in report_obj.keys():
            today = datetime.datetime.now()
            date_day = datetime.datetime.strptime(date, '%Y-%m-%dZ')
            days_between = (today - date_day).days
            if days_between > days:
                continue
            else:
                return_obj[date] = report_obj[date]


    return return_obj

# end keep_recent_days( uniq_dates, days ):

def get_ticker_row( report_obj, uniq_dates, ticker):

    row = ""
    row = row + "<tr>\n"
    row = row + "<td>" + ticker + "</td>\n"
    for date in uniq_dates:
        if ticker in report_obj[date].keys():
            bgcolor = ""
            col = ""
            for trade in report_obj[date][ticker]:
                col = col + trade["ticker"] + " " + \
                      trade["direction"] + " " + \
                      trade["fund"] + "<br>"
                if trade["direction"] == "Buy":
                    bgcolor = "green"
                elif trade["direction"] == "Sell":
                    bgcolor = "red"
                        
            row = row \
                + "<td bgcolor=\"" + bgcolor + "\" style=\"color:#ffffff\">" \
                + col \
                + "</td>\n"
        else:
            row = row \
                + "<td>" \
                + "" \
                + "</td>\n"
            
    row = row + "</tr>\n"

    return row
# end get_program_row()

def get_head_row(uniq_dates):

    row = ""
    row = row + "<th>\n"
    for date in uniq_dates:
        row = row + "<td>" + date + "</td>\n"

    row = row + "</th>\n"

    return row
# end get_head_row()


main()
