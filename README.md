# Zuri-Training-Making-Budget-with-Classes
Submission for the assignment requiring creation of a Budget using OOP 


The file is made up of a class called Budget containing its own methods - Withdraw, deposit, balance and transfer.

In the init method , an empty list called transaction records is created.
In deposit, we have attributes ammount and description with a line of code which literally appends the passed instatiated values into the empty list . 
In the withdrawal method , it does a similar funtion to the above , only that it holds the negative value of the ammount passed. 

In the balance method , first an initailisation of varibale total is done with it being set to 0, then we loop to the transaction list containing dictionaries of keys and values.
The very next line under this performns an augmented assignmnet whereas the key - item["ammount"] holding withdrawal and deposit value is picked
Tabbing out of the for loop, we have a return value which gives the final value of total. 

In the transfer method , it takes the self attribute as well as ammount and destination with the codes under it working under the same principle as the two above.
Just that, in this case , the self.withdraw takes an ammount and destination.name variable implying the soon to be instatiated objects.
Then the other line , works with the .deposit principle taking an ammount and the proposed self.name all of which are stored in the "total" list of dictionaries. 

finally to end the class is the __str__(self): method which literally prints out the desired output of the user. In this case; Budget name.
A for loop is made underneath to acess the "description " as well as the "ammount" values these keys hold with a formatting adjustment to make the output much more presentable. 

Now that we are out of the class ; the rest of the code is just instantianting and carrying out deposit , withdrawal and transfer functions. 
