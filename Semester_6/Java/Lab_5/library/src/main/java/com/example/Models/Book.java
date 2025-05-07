package com.example.Models;

public class Book {
    private  String title;
    private  String author;
    private  String genre;
    private  int pages;

    public Book() {}
    
    public Book(String title, String author, String genre, int pages) {
        this.title = title;
        this.author = author;
        this.genre = genre;
        this.pages = pages;
    }

    public String getTitle() {
        return title;
    }

    public String getAuthor() {
        return author;
    }

    public String getGenre() {
        return genre;
    }

    public int getPages() {
        return pages;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public void setGenre(String genre) {
        this.genre = genre;
    }

    public void setPages(int pages) {
        this.pages = pages;
    }
    
}
