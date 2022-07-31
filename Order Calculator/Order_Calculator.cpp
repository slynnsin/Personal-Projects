/************************************************************
Sarah Sindeband
Date: 9/22/21
Course: C0P3014
Description: This program will calculate the online order cost details based on the information in the file purchaseOrderData.txt


*************************************************************/
#include <iostream> //standard library for i/o
#include <fstream>//you must include this library if you wish to do file i/o
#include <string> // always include this when you use the string class

using namespace std;

/*********************************************************
//Following is the declaration of a order record
**********************************************************/
struct orderRecord
{
	string cellNum;
	string itemNum;
	int quantity = 0;
	double price = 0.0;
	int locationID = 0;
	double taxRate = 0.0;
	double tax = 0.0;
	double netCost = 0.0;
	double totalCost = 0.0;
};

//Declaration / Prototypes for functions

void DataFromFile(ifstream&, orderRecord&);
//Precondition:  The file will be connected and a valid order record must have been delcared.
//Postcondition:  One line of data has been read from the file.
//Description:  Read the data from one order record in the file.

void PrintToScreen(const orderRecord&);
//Precondition:  Data from the file will be processed.
//Postcondition:  Processed data will be printed to the screen.
//Description:  This function will print the order information and calculations to the screen.

void ProcessData(orderRecord&);
//Precondition:  Tax rate from the orderRecord will be used for calculations.
//Postcondition:  Calculations are completed for the information in the orderRecord based on the tax rate.
//Description:  Get the tax rate and execute the calculations.

void GetTaxRate(double&, int);
//Precondition:  The two paramaters will be declared as a double for the tax rate and int for the location ID number from the data file.
//Postcondition:  Tax rate will be set inside the function based on the location ID number and calculated.
//Description:  Tax rate will be calcualted by the location ID number found in the data file.


int main()
{
	//Greet the user
	string name;
	cout << "\n\nEnter your first name: ";
	cin >> name;
	cout << name << ", Let's get started processing the file data." << endl;
	//Print the column headings
	cout << "Phone Number\tItem Number\tQty\tPrice\tLocID\tRate\tTax\tNet\tTotal\n";

	//Declare the orderRecord
	orderRecord recordData;

	ifstream in;    //declaring an input file stream
	in.open("purchaseOrderData.txt"); //connect to the input file add the file name

	if (in.fail())
	{
		cout << "Input file did not open correctly" << endl;
	}
	else
	{
		//cout << "connected to the input file" << endl;
	while (!in.eof()) //has not reached the end of the file
	{
		DataFromFile(in, recordData);
		GetTaxRate(recordData.taxRate, recordData.locationID);
		ProcessData(recordData);
		PrintToScreen(recordData);
	}
	}

	in.close();
	//say goodbye to the user
	cout << endl << name << ", have a nice day!\n\n";
	return 0;
}


//Function Implementations

void DataFromFile(ifstream& in, orderRecord& currentRecord)
//Description:  Read the data from one order record from the file.
{
	in >> currentRecord.cellNum; // in instead of cin for file input stream, currentRecord with info from orderRecord
	in >> currentRecord.itemNum;
	in >> currentRecord.quantity;
	in >> currentRecord.price;
	in >> currentRecord.locationID;
}

void ProcessData(orderRecord& currentRecord)
//Description:  Get the tax rate and make the calculations.
{
	if (currentRecord.locationID <= 0)
	{
		cout << "\nZERO or a negative number for the location ID is not a valid entry.\n";
		currentRecord.price = 0.0;
		currentRecord.locationID = 0;
		currentRecord.taxRate = 0.0;
		currentRecord.tax = 0.0;
		currentRecord.netCost = 0.0;
		currentRecord.totalCost = 0.0;
	}
	else
	{
		currentRecord.tax = currentRecord.price * currentRecord.quantity * currentRecord.taxRate;
		currentRecord.netCost = currentRecord.price * currentRecord.quantity;
		currentRecord.totalCost = currentRecord.tax + currentRecord.netCost;
	}
	//Call the GetTaxRate function to get the tax rate based on the currentRecord.locationID,
	//calculate the tax, netCost, and totalCost of the currentRecord
	GetTaxRate(currentRecord.taxRate, currentRecord.locationID);
}

void GetTaxRate(double& taxRate, int locationID)
//Description:  Finds the tax rate based on the locationID.
{
	//use the location ID to set the tax rate
	if (locationID < 0) // invalid location
		taxRate = 0;
	else if (locationID >= 1 && locationID <= 15)
		taxRate = .0444;
	else if (locationID >= 16 && locationID <= 30)
		taxRate = .0525;
	else if (locationID >= 31 && locationID <= 45)
		taxRate = .061;
	else if (locationID > 45)
		taxRate = .0935;
}

void PrintToScreen(const orderRecord& currentRecord)
//Description:  Prints the results onto the screen.
{
	//set the number of decimal places for doubles
	cout.setf(ios::fixed);
	cout.setf(ios::showpoint);
	cout.precision(2); //2 decimal places

	// display the results here

	cout << currentRecord.cellNum << "\t";
	cout << currentRecord.itemNum << "\t";
	cout << currentRecord.quantity << "\t";
	cout << currentRecord.price << "\t";
	cout << currentRecord.locationID << "\t";

	cout.precision(4);//4 decimal places
	cout << currentRecord.taxRate << "\t";

	cout.precision(2);//back to 2 decimal places
	cout << currentRecord.tax << "\t";
	cout << currentRecord.netCost << "\t";
	cout << currentRecord.totalCost << "\t" << endl;
}