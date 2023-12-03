#include <iostream>
#include"Factory.h"
int main()
{
    setlocale(LC_ALL, "ru");

    Window window;
    Linux linux;
    Mac mac;

   

    std::cout << "Windows: " << std::endl;
    auto window_7 = window.creatComboBox();

    window_7->set("Windows 7");
    window_7->get();
    window_7->infComboBox();

    auto window_7_ = window.creatDataEdit();

    window_7_->set("Window 7: 22.22.22");
    window_7_->get();

    std::cout << std::endl;
    std::cout << "Linux: " << std::endl;

    auto linux_ = linux.creatRichTextBox();

    linux_->set("Linux234");
    linux_->get();

    std::cout << std::endl;
    std::cout << "Mac: " << std::endl;

    auto mac_ = mac.creatRichTextBox();

    mac_->set("MAC MAC");
    mac_->get();
    mac_->infRichTextBox();

}