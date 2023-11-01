package org.velezreyes.quiz.question6;

public class VendingMachineImpl implements VendingMachine{

  int quarters = 0;

  public static VendingMachine getInstance() {
    //We have to return an instance, c'est à dire a new object
    VendingMachineImpl object = new VendingMachineImpl();
    return object;
  }

  @Override
  public void insertQuarter() {
    //Inserts 25c, increments the quarters variable
    this.quarters += 1;
  }

  @Override
  public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
    DrinkImpl drinkGenerated = new DrinkImpl("", false);
      if(name.equals("ScottCola")){
        if(this.quarters>=3){
          drinkGenerated.name=name;
          drinkGenerated.fizzy=true;
          this.quarters-=3;
          return drinkGenerated;
        }
        else{
          throw new NotEnoughMoneyException();
        }
      }
      if(name.equals("KarenTea")){
        if(this.quarters>=4){
          drinkGenerated.name=name;
          this.quarters-=4;
          return drinkGenerated;
        }else{
          throw new NotEnoughMoneyException();
        }
      }
      else{
        throw new UnknownDrinkException();
      }
    
  }
}
