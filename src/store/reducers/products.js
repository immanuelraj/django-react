import * as actionTypes from "../actions/actionTypes";
import { updateObject } from "../utility";

const initialState = {
  products: [],
  currentProduct: {},
  error: null,
  loading: false
};

const getProductListStart = (state, action) => {
  return updateObject(state, {
    error: null,
    loading: true
  });
};

const getProductListSuccess = (state, action) => {
  return updateObject(state, {
    products: action.products,
    error: null,
    loading: false
  });
};

const getProductListFail = (state, action) => {
  return updateObject(state, {
    error: action.error,
    loading: false
  });
};

const getProductDetailStart = (state, action) => {
  return updateObject(state, {
    error: null,
    loading: true
  });
};

const getProductDetailSuccess = (state, action) => {
  return updateObject(state, {
    currentProduct: action.product,
    error: null,
    loading: false
  });
};

const getProductDetailFail = (state, action) => {
  return updateObject(state, {
    error: action.error,
    loading: false
  });
};

const createProductStart = (state, action) => {
  return updateObject(state, {
    error: null,
    loading: true
  });
};

const createProductSuccess = (state, action) => {
  return updateObject(state, {
    error: null,
    loading: false
  });
};

const createProductFail = (state, action) => {
  return updateObject(state, {
    error: action.error,
    loading: false
  });
};

const reducer = (state = initialState, action) => {
  switch (action.type) {
    case actionTypes.GET_PRODUCT_LIST_START:
      return getProductListStart(state, action);
    case actionTypes.GET_PRODUCTS_LIST_SUCCESS:
      return getProductListSuccess(state, action);
    case actionTypes.GET_PRODUCTS_LIST_FAIL:
      return getProductListFail(state, action);
    case actionTypes.GET_PRODUCT_DETAIL_START:
      return getProductDetailStart(state, action);
    case actionTypes.GET_PRODUCT_DETAIL_SUCCESS:
      return getProductDetailSuccess(state, action);
    case actionTypes.GET_PRODUCT_DETAIL_FAIL:
      return getProductDetailFail(state, action);
    case actionTypes.CREATE_PRODUCT_START:
      return createProductStart(state, action);
    case actionTypes.CREATE_PRODUCT_SUCCESS:
      return createProductSuccess(state, action);
    case actionTypes.CREATE_PRODUCT_FAIL:
      return createProductFail(state, action);
    default:
      return state;
  }
};

export default reducer;
