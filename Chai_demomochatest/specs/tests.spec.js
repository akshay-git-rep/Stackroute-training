const chai = require("chai");
const assert = chai.assert;
const expect = chai.expect;
const calc = require("../src/calculator");
before(() => {
  console.log("Before first test");
});
after(() => {
  console.log("After last test");
});
beforeEach(() => {
  console.log("Starting a test");
});
afterEach(() => {
  console.log("Completing a test");
});
describe("should be failing", () => {
  it("2 should be equals to 2", () => {
    assert.equal(2, 2);
  });
});
describe("5+5 Equals 10", () => {
  it("5+5 should be equals to 10", () => {
    expect(calc.add(5, 5)).to.equal(10);
  });
});
describe("Addition", () => {
  it("1+1 should be equals to 2", () => {
    // Arrange
    let expected = 2;
    // Act
    let actual = calc.add(1, 1);
    // Assert
    assert.equal(actual, expected);
  });
  it("2+2 should be equals to 4", () => {
    // Arrange
    let expected = 4;
    // Act
    let actual = calc.add(2, 2);
    // Assert
    assert.equal(actual, expected);
  });
});
describe("Subtraction", () => {
  it("5-2 should be equals to 3", () => {
    let sub = calc.sub(5, 2);
    assert.equal(sub, 3);
  });
});


// https://itnext.io/how-to-make-tests-using-chai-and-mocha-e9db7d8d48bc
// npm install
// npm test OR npm run test