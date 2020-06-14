import * as actionTypes from "../actions/actionTypes";
import { updateObject } from "../utility";

const initialState = {
  orders: [],
  currentOrder: {},
  error: null,
  loading: false
};

const getOrderListStart = (state, action) => {
  return updateObject(state, {
    error: null,
    loading: true
  });
};

const getOrderListSuccess = (state, action) => {
  return updateObject(state, {
    assignments: action.assignments,
    error: null,
    loading: false
  });
};

const getOrderListFail = (state, action) => {
  return updateObject(state, {
    error: action.error,
    loading: false
  });
};

const getOrderDetailStart = (state, action) => {
  return updateObject(state, {
    error: null,
    loading: true
  });
};

const getOrderDetailSuccess = (state, action) => {
  return updateObject(state, {
    currentOrder: action.order,
    error: null,
    loading: false
  });
};

const getOrderDetailFail = (state, action) => {
  return updateObject(state, {
    error: action.error,
    loading: false
  });
};

const reducer = (state = initialState, action) => {
  switch (action.type) {
    case actionTypes.GET_ORDER_LIST_START:
      return getOrderListStart(state, action);
    case actionTypes.GET_ORDERS_LIST_SUCCESS:
      return getOrderListSuccess(state, action);
    case actionTypes.GET_ORDERS_LIST_FAIL:
      return getOrderListFail(state, action);
    case actionTypes.GET_ORDER_DETAIL_START:
      return getOrderDetailStart(state, action);
    case actionTypes.GET_ORDER_DETAIL_SUCCESS:
      return getOrderDetailSuccess(state, action);
    case actionTypes.GET_ORDER_DETAIL_FAIL:
      return getOrderDetailFail(state, action);
    default:
      return state;
  }
};

export default reducer;