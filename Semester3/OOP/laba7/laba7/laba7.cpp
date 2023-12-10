#include <iostream>
#include "MemoryUserRepository.h"
int main()
{
    setlocale(LC_ALL, "ru");
    User user1;
    user1.setId(1221);
    user1.setName("Вася");
    user1.setPhone("79008787652");
    user1.setGender(Male);
    user1.setEmail("Vasya01.@mail.ru");
    user1.setCity("Калининград");

    User user2;
    user2.setId(12232);
    user2.setName("Даша");
    user2.setPhone("79119020203");
    user2.setGender(Female);
    user2.setEmail("Dashalyagushka04.@gmail.com");
    user2.setCity("Москва");

    User user3;
    user3.setId(16563);
    user3.setName("Рома");
    user3.setPhone("79007658765");
    user3.setGender(Male);
    user3.setEmail("VeROnd1.@mail.ru");
    user3.setCity("Калининград");

    User user4;
    user4.setId(13232);
    user4.setName("Света");
    user4.setPhone("79008233243");
    user4.setGender(Female);
    user4.setEmail("Svetbest1192.@mail.ru");
    user4.setCity("Калининград");

    User user5;
    user5.setId(156242);
    user5.setName("Вася");
    user5.setPhone("79008787651");
    user5.setGender(Male);
    user5.setEmail("Vasya987623.@dmail.com");
    user5.setCity("Москва");

    MemoryUserRepository user_reposit;
    user_reposit.Add(&user1);
    user_reposit.Add(&user2);
    user_reposit.Add(&user3);
    user_reposit.Add(&user4);


    User* user1_by_ID = user_reposit.getById(1221);
    cout << "ID 1221: " << endl 
            << user1_by_ID->getName() << endl
            << user1_by_ID->getGender() << endl
            << user1_by_ID->getCity() << endl
            << user1_by_ID->getPhone() << endl
            << user1_by_ID->getEmail() << endl;
    cout  << "------------------------------------------------------" << endl;
    User* user2_by_Name = user_reposit.getByName("Рома");
    cout << "Рома: " << endl
        << user2_by_Name->getId() << endl
        << user2_by_Name->getGender() << endl
        << user2_by_Name->getCity() << endl
        << user2_by_Name->getPhone() << endl
        << user2_by_Name->getEmail() << endl;
    cout << "------------------------------------------------------" << endl;
    User* user3_by_Email = user_reposit.getByEmail("Dashalyagushka04.@gmail.com");
    cout << "Dashalyagushka04.@gmail.com: " << endl
        << user3_by_Email->getId() << endl
        << user3_by_Email->getName() << endl
        << user3_by_Email->getGender() << endl
        << user3_by_Email->getCity() << endl
        << user3_by_Email->getPhone() << endl;
    cout << "------------------------------------------------------" << endl;
    vector<User*> user4_by_Gender = user_reposit.getByGender(Female);
    cout << "Female: " << endl;
    for (int i = 0; i < user4_by_Gender.size(); i++)
    {
        cout << user4_by_Gender[i]->getId() << endl
            << user4_by_Gender[i]->getName() << endl
            << user4_by_Gender[i]->getCity() << endl
            << user4_by_Gender[i]->getPhone() << endl
            << user4_by_Gender[i]->getEmail() << endl << endl;
    }
    
    user_reposit.Delete(&user1);
}
