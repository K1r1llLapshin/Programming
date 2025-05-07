module com.example.Windows {
    requires javafx.controls;
    requires javafx.fxml;
    requires java.sql;
    
    opens com.example.Windows to javafx.fxml;
    exports com.example.Windows;
}
