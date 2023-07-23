import Currency from "./3-currency";

export default class Pricing {
  constructor(amount, currency) {
    this.amount = amount;
    this.currency = currency;
  }

  set(newAmount) {
    if (typeof newAmount != 'number') {
      throw new Error('Amount must be a number');
    }
    this._amount = newAmount;
  }

  displayFullPrice() {
    return `${this.amount} ${this.currency.name} (${this.currency.code})`
  }

  static convertPrice(amount, conversionRate) {
    if (typeof amount !== 'number' && typeof conversionRate !== 'number') {
      throw new Error('Amout must be a number');
    }
    return amount * conversionRate;
  }
}
