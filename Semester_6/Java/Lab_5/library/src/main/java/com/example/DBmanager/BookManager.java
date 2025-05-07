package com.example.DBmanager;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

import com.example.Models.Book;

public class BookManager extends DatabaseManager {
    
    // Добавление новой книги в базу данных
    public void addBook(Book book) throws SQLException {
        validateConnection();
        
        String sql = "INSERT INTO books (title, author, genre, pages) VALUES (?, ?, ?, ?)";
        
        try (PreparedStatement stmt = connection.prepareStatement(sql)) {
            stmt.setString(1, book.getTitle());
            stmt.setString(2, book.getAuthor());
            stmt.setString(3, book.getGenre());
            stmt.setInt(4, book.getPages());
            stmt.executeUpdate();
        }
        catch (SQLException e) {
            System.err.println("Ошибка при добавлении книги пользователя: " + e.getMessage());
        }
    }
    
    // Получение книги по её ID
    public Book getBook(int bookId) throws SQLException {
        validateConnection();  
        String sql = "SELECT id, title, author, genre, pages FROM books WHERE id = ?";  
        try (PreparedStatement stmt = connection.prepareStatement(sql)) {
            stmt.setInt(1, bookId);
            
            try (ResultSet rs = stmt.executeQuery()) {
                if (rs.next()) {
                    Book book = new Book(
                        rs.getString("title"),
                        rs.getString("author"),
                        rs.getString("genre"),
                        rs.getInt("pages")
                    );
                    return book;
                }
            }
            catch (SQLException e) {
                System.err.println("Ошибка при выполнении запроса: " + e.getMessage());
            }
        }
        catch (SQLException e) {
            System.err.println("Ошибка при выполнении запроса: " + e.getMessage());
        }
        return null; // Если книга не найдена
    }
    
    // Получение ID книги
    public int getBookId(Book book) throws SQLException {
        validateConnection();  
        String sql = "SELECT id FROM books WHERE title = ? AND author = ? AND genre = ? AND pages = ?";  
        try (PreparedStatement stmt = connection.prepareStatement(sql)) {
            stmt.setString(1, book.getTitle());
            stmt.setString(2, book.getAuthor());
            stmt.setString(3, book.getGenre());
            stmt.setInt(4, book.getPages());

            try (ResultSet rs = stmt.executeQuery()) {
                if (rs.next()) 
                    return rs.getInt("id");
            }
            catch (SQLException e) {
                System.err.println("Ошибка при выполнении запроса: " + e.getMessage());
            }
        }
        catch (SQLException e) {
            System.err.println("Ошибка при выполнении запроса: " + e.getMessage());
        }
        return 0;
    }   

    // Обновление информации о книге
    public void updateBook(Book book, int bookId) throws SQLException {
        validateConnection();
        
        String sql = "UPDATE books SET title = ?, author = ?, genre = ?, pages = ? WHERE id = ?";
        
        try (PreparedStatement stmt = connection.prepareStatement(sql)) {
            stmt.setString(1, book.getTitle());
            stmt.setString(2, book.getAuthor());
            stmt.setString(3, book.getGenre());
            stmt.setInt(4, book.getPages());
            stmt.setInt(5, bookId);
            stmt.executeUpdate();
        }
    }
    
    // удаление книги из базы данных
    public void deleteBook(int bookId) throws SQLException {
        validateConnection();
        
        String sql = "DELETE FROM books WHERE id = ?";
        
        try (PreparedStatement stmt = connection.prepareStatement(sql)) {
            stmt.setInt(1, bookId);
            stmt.executeUpdate();
        }
        catch (SQLException e) {
            System.err.println("Ошибка при выполнении запроса: " + e.getMessage());
        }
    }
    
}