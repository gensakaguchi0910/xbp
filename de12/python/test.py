import tkinter as tk
import webbrowser

def open_url1():
    url1 = 'https://store-tsutaya.tsite.jp/item/search_result.html?k=&i=226'  
    webbrowser.open_new(url1)
def open_url2():
    url2 = 'https://search.yurindo.bscentral.jp/search' 
    webbrowser.open_new(url2)
def open_url3():
    url3 = 'https://www.miraiyashoten.co.jp/search/'  
    webbrowser.open_new(url3)
def open_url4():
    url4 = 'https://www.books-sanseido.jp/booksearch/BookSearchInit.action'  
    webbrowser.open_new(url4)
def open_url5():
    url5 = 'https://www.search.kumabook.com/kumazawa/html/'  
    webbrowser.open_new(url5)


app = tk.Tk()
app.title("在庫確認アプリ")


button1 = tk.Button(app, text="蔦屋書店", command=open_url1)
button1.pack(pady=20)

button2 = tk.Button(app, text="有隣堂", command=open_url2)
button2.pack(pady=20)

button3 = tk.Button(app, text="未来屋書店", command=open_url3)
button3.pack(pady=20)

button4 = tk.Button(app, text="三省堂書店", command=open_url4)
button4.pack(pady=20)

button5 = tk.Button(app, text="くまざわ書店", command=open_url5)
button5.pack(pady=20)

app.mainloop()
