// Scan # 2 
#include <iostream>
#include <vector>

using namespace std;

class Account;
class Transaction
{       
public:
    Account *account;
    Transaction(Account *a);
    virtual void execute();
};

class Account
{
private:
    string accountNumber;
    vector<Transaction*> transactionHistory;
public:
    double balance;
    Account(string, double);
    void displayTransactionHistory();
    void addTransactionToHistory(Transaction*);
};

Transaction::Transaction(Account *a)
{
    account = a;
}

Account::Account(string accNum, double bal)
{
    accountNumber = accNum;
    balance = bal;
    cout << "Account (" << accountNumber << ") has been created and current balance is: $" << balance << endl; 
}

void Account::displayTransactionHistory()
{
    cout << "Transaction History for Account (" << accountNumber << "):" << endl;
    for (Transaction* t : transactionHistory)
    {
        t->execute();
    }
}

void Account::addTransactionToHistory(Transaction* transaction)
{
    transactionHistory.push_back(transaction);
}

class Deposit : public Transaction
{
private:
    double amount;
public:
    Deposit(double, Account*);
    void execute();
};

Deposit::Deposit(double amo, Account* acc) : Transaction(acc)
{
    amount = amo;
    acc->balance += amount;
}

void Deposit::execute()
{
    cout << "Successful deposit operation and current balance is: $" << account->balance << endl;
}

class Withdrawal : public Transaction
{
private:
    double amount;
public:
    Withdrawal(double, Account*);
    void execute();
};

Withdrawal::Withdrawal(double am, Account* ac) : Transaction(ac)
{
    amount = am;
    ac->balance -= amount;
}

void Withdrawal::execute()
{
    cout << "Successful withdrawal operation and current balance is: $" << account->balance << endl;
}

void performTransaction(Transaction *T)
{
    T->execute();
}

int main()
{
    Account A("ABC_123", 0);

    Deposit D(1000,&A);
    A.addTransactionToHistory(&D);
    performTransaction(&D);

    Withdrawal W(500, &A);
    A.addTransactionToHistory(&W);
    performTransaction(&W);

    A.displayTransactionHistory();

    return 0;
}
