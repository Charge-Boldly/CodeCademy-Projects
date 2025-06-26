import { store, increment, decrement } from "./store";

// Define your change listener function here.
const printCountStatus = () => {
  console.log(`The count is ${store.getState()}`);
};

// Subscribe change listener function to the store here
store.subscribe(printCountStatus);

store.dispatch(decrement()); // store.getState() === -1
store.dispatch(increment()); // store.getState() === 0
store.dispatch(increment()); // store.getState() === 1
