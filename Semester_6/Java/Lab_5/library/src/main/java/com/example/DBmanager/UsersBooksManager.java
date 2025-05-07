package com.example.DBmanager;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class UsersBooksManager extends DatabaseManager{
    
    //Добавить книгу в таблицу книги-пользователь
     public void addUserBook(String userId, int bookId, String status, String dateStart, String dateEnd, String description) throws SQLException {
        validateConnection();
        
        String sql = "INSERT INTO users_books (user_login, book_id, status, date_start, date_end, description) VALUES (?, ?, ?, ?, ?, ?)";
        
        try (PreparedStatement stmt = connection.prepareStatement(sql)) {
            stmt.setString(1, userId);
            stmt.setInt(2, bookId);
            stmt.setString(3, status);
            stmt.setString(4, dateStart);
            stmt.setString(5, dateEnd);
            stmt.setString(6, description);
            stmt.executeUpdate();
        }
        catch (SQLException e) {
            System.err.println("Ошибка при добавлении книги пользователя: " + e.getMessage());
        }
    }
    
    //Удалить книгу из таблицы книги-пользователь
    public void deleteUserBook(String userId, int bookID) throws SQLException {
        validateConnection();

        String sql = "DELETE FROM users_books WHERE user_login = ? AND book_id = ?";

        try (PreparedStatement stmt = connection.prepareStatement(sql)) {
            stmt.setString(1, userId);
            stmt.setInt(2, bookID);
            stmt.executeUpdate();
        } 
        catch (SQLException e) {
            System.err.println("Ошибка при удалении книги пользователя: " + e.getMessage());
        }
    }
    
    //Получить список книг пользователя
    public List<Integer> getBooksId(String userId) throws SQLException {
        validateConnection();
        List<Integer> bookIds = new ArrayList<>();
        
        String sql = "SELECT book_id FROM users_books WHERE user_login = ?";
        
        try (PreparedStatement stmt = connection.prepareStatement(sql)) {
            stmt.setString(1, userId);
            
            try (ResultSet rs = stmt.executeQuery()) {
                while (rs.next()) {
                    bookIds.add(rs.getInt("book_id"));
                }
            }
        }
        return bookIds;
    }

    //Получить записи пользователя
    public List<List<String>> getUserInformation(String userId) throws SQLException {
        validateConnection();
        List<List<String>> informations = new ArrayList<>();
        
        String sql = "SELECT book_id, status, date_start, date_end, description FROM users_books WHERE user_login = ?";
        
        try (PreparedStatement stmt = connection.prepareStatement(sql)) {
            stmt.setString(1, userId);
            
            try (ResultSet rs = stmt.executeQuery()) {
                while (rs.next()) {  // Используем while для обработки всех записей
                    List<String> bookInfo = new ArrayList<>();
                    
                    // Добавляем информацию о каждой книге
                    bookInfo.add(rs.getString("book_id"));
                    bookInfo.add(rs.getString("status"));
                    
                    // Обрабатываем возможные NULL значения для дат
                    String startDate = rs.getString("date_start");
                    bookInfo.add(startDate != null ? startDate : "");
                    
                    String endDate = rs.getString("date_end");
                    bookInfo.add(endDate != null ? endDate : "");
                    
                    String description = rs.getString("description");
                    bookInfo.add(description != null ? description : "");

                    informations.add(bookInfo);
                }
            }
        }
        
        return informations;
    }
  
    //Обновить запись в таблице книги-пользователи
    public void updateUserBook(String userId, int bookId, String status, String dateStart, String dateEnd, String description) throws SQLException {
        validateConnection();
        
        String sql = "UPDATE users_books SET status = ?, date_start = ?, date_end = ?, description = ? WHERE user_login = ? AND book_id = ?";
        
        try (PreparedStatement stmt = connection.prepareStatement(sql)) {
            stmt.setString(1, status);
            stmt.setString(2, dateStart);
            stmt.setString(3, dateEnd);
            stmt.setString(4, description);
            stmt.setString(5, userId);
            stmt.setInt(6, bookId);
            stmt.executeUpdate();
        }
        catch (SQLException e) {
            System.err.println("Ошибка при обновлении записи книги пользователя: " + e.getMessage());
        }
    }

}
