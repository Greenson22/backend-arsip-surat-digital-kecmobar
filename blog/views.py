from django.shortcuts import render

def index(response):
	context = {
		"judul" : "Sebuah Blog",
		"isi"	: "Ini hanyalah sebuah blog"
	}
	return render(response, "blog_index.html", context)
