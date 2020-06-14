import axios from "axios";
import * as actionTypes from "./actionTypes";

const getOrderListStart = () => {
  return {
    type: actionTypes.GET_ORDER_LIST_START
  };
};

const getOrderListSuccess = order => {
return {
  type: actionTypes.GET_ORDERS_LIST_SUCCESS,
  order
};
};

const getOrderListFail = error => {
return {
  type: actionTypes.GET_ORDERS_LIST_FAIL,
  error: error
};
};

export const getOrders = (token, id) => {
return dispatch => {
  dispatch(getOrderListStart());
  axios.defaults.headers = {
    "Content-Type": "application/json",
    Authorization: `Token ${token}`
  };
  axios
    .get(`http://127.0.0.1:8000/order/`)
    .then(res => {
      const order = res.data;
      dispatch(getOrderListSuccess(order));
    })
    .catch(err => {
      dispatch(getOrderListFail());
    });
};
};

const getOrderDetailStart = () => {
    return {
      type: actionTypes.GET_ORDER_DETAIL_START
    };
  };
  
const getOrderDetailSuccess = order => {
  return {
    type: actionTypes.GET_ORDER_DETAIL_SUCCESS,
    order
  };
};

const getOrderDetailFail = error => {
  return {
    type: actionTypes.GET_ORDER_DETAIL_FAIL,
    error: error
  };
};

export const getOrderDetail = (token, id) => {
  return dispatch => {
    dispatch(getOrderDetailStart());
    axios.defaults.headers = {
      "Content-Type": "application/json",
      Authorization: `Token ${token}`
    };
    axios
      .get(`http://127.0.0.1:8000/order/${id}/`)
      .then(res => {
        const order = res.data;
        dispatch(getOrderDetailSuccess(order));
      })
      .catch(err => {
        dispatch(getOrderDetailFail());
      });
  };
};