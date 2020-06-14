import axios from "axios";
import * as actionTypes from "./actionTypes";

const getProductListStart = () => {
  return {
    type: actionTypes.GET_PRODUCT_LIST_START
  };
};

const getProductListSuccess = products => {
  return {
    type: actionTypes.GET_PRODUCTS_LIST_SUCCESS,
    products
  };
};

const getProductListFail = error => {
  return {
    type: actionTypes.GET_PRODUCTS_LIST_FAIL,
    error: error
  };
};

export const getProducts = token => {
  return dispatch => {
    dispatch(getProductListStart());
    axios.defaults.headers = {
      "Content-Type": "application/json",
      Authorization: `Token ${token}`
    };
    axios
      .get("http://127.0.0.1:8000/grocery/product/")
      .then(res => {
        console.log(res.data.results)
        const products = res.data.results;
        dispatch(getProductListSuccess(products));
      })
      .catch(err => {
        dispatch(getProductListFail());
      });
  };
};


const getProductDetailStart = () => {
    return {
      type: actionTypes.GET_PRODUCT_DETAIL_START
    };
  };
  
  const getProductDetailSuccess = product => {
    return {
      type: actionTypes.GET_PRODUCT_DETAIL_SUCCESS,
      product
    };
  };
  
  const getProductDetailFail = error => {
    return {
      type: actionTypes.GET_PRODUCT_DETAIL_FAIL,
      error: error
    };
  };
  
  export const getProductsDetail = (token, id) => {
    return dispatch => {
      dispatch(getProductDetailStart());
      axios.defaults.headers = {
        "Content-Type": "application/json",
        Authorization: `Token ${token}`
      };
      axios
        .get(`http://127.0.0.1:8000/product/${id}/`)
        .then(res => {
          const product = res.data;
          dispatch(getProductDetailSuccess(product));
        })
        .catch(err => {
          dispatch(getProductDetailFail());
        });
    };
  };
  
  const createProductStart = () => {
    return {
      type: actionTypes.CREATE_PRODUCT_START
    };
  };
  
  const createProductSuccess = assignment => {
    return {
      type: actionTypes.CREATE_PRODUCT_SUCCESS,
      assignment
    };
  };
  
  const createProductFail = error => {
    return {
      type: actionTypes.CREATE_PRODUCT_FAIL,
      error: error
    };
  };
  
  export const createProduct = (token, product) => {
    return dispatch => {
      dispatch(createProductStart());
      axios.defaults.headers = {
        "Content-Type": "application/json",
        Authorization: `Token ${token}`
      };
      axios
        .post(`http://127.0.0.1:8000/grocery/product/`, product)
        .then(res => {
          dispatch(createProductSuccess());
        })
        .catch(err => {
          dispatch(createProductFail());
        });
    };
  };