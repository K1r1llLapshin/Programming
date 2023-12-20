#include "User.h"

int  User::getId()
{
    return mId;
}

string User::getName()
{
    return mName;
}

string User::getEmail()
{
    return mEmail;
}

string User::getPhone()
{
    return mPhone;
}

string User::getCity()
{
    return mCity;
}

Gender User::getGender()
{
    return mGender;
}

void User::setId(int mId)
{
    this->mId = mId;
}

void User::setName(const string& mName)
{
    this->mName = mName;
}

void User::setEmail(const string& mEmail)
{
    this->mEmail = mEmail;
}

void User::setPhone(const string& mPhone)
{
    this->mPhone = mPhone;
}

void User::setCity(const string& mCity)
{
    this->mCity = mCity;
}

void User::setGender(Gender mGender)
{
    this->mGender = mGender;
}
