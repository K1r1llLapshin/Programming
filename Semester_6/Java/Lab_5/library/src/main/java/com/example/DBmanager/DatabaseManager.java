package com.example.DBmanager;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;



public class DatabaseManager {
    protected Connection connection;

    // Подключение к базе данных
    public void connect(String databasePath) throws SQLException {
        try {
            this.connection = DriverManager.getConnection("jdbc:sqlite:" + databasePath);
            System.out.println("Подключение к базе данных успешно!");
        } 
        catch (SQLException e) {
            System.err.println("Ошибка подключения к базе данных: " + e.getMessage());
            throw e;
        }
    }

    // Проверка подключения к базе данных
    public  void validateConnection() throws SQLException {
        if (connection == null || connection.isClosed()) {
            throw new SQLException("Соединение с базой данных не установлено");
        }
    }

    // Закрытие соединения с базой данных
    public void close() {
        try {
            if (connection != null && !connection.isClosed()) {
                connection.close();
                System.out.println("Соединение с базой данных закрыто");
            }
        } catch (SQLException e) {
            System.err.println("Ошибка при закрытии соединения: " + e.getMessage());
        }
    }

    // Проверка существования записи в таблице по значению указанного столбца
    public boolean exists(String tableName, String columnName, Object value) throws SQLException {
        validateConnection();
        String sql = "SELECT 1 FROM " + tableName + " WHERE " + columnName + " = ?";
        
        try (PreparedStatement stmt = connection.prepareStatement(sql)) {
            stmt.setObject(1, value);
            try (ResultSet rs = stmt.executeQuery()) {
                return rs.next();
            }
        }
    }

}