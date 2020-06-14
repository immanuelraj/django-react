import * as actionTypes from "../actions/actionTypes";
import { updateObject } from "../utility";

const initialState = {
  categories: [],
  currentOrder: {},
  error: null,
  loading: false
};

const getCategoryListStart = (state, action) => {
  return updateObject(state, {
    error: null,
    loading: true
  });
};

const getCategoryListSuccess = (state, action) => {
  return updateObject(state, {
    categories: action.categories,
    error: null,
    loading: false
  });
};

const getCategoryListFail = (state, action) => {
  return updateObject(state, {
    error: action.error,
    loading: false
  });
};

const reducer = (state = initialState, action) => {
  switch (action.type) {
    case actionTypes.GET_ORDER_LIST_START:
      return getCategoryListStart(state, action);
    case actionTypes.GET_ORDERS_LIST_SUCCESS:
      return getCategoryListSuccess(state, action);
    case actionTypes.GET_ORDERS_LIST_FAIL:
      return getCategoryListFail(state, action);
    default:
      return state;
  }
};

export default reducer;