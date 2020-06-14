import axios from "axios";
import * as actionTypes from "./actionTypes";

const getCategoryListStart = () => {
  return {
    type: actionTypes.GET_CATEGORY_LIST_START
  };
};

const getCategoryListSuccess = categories => {
  return {
    type: actionTypes.GET_CATEGORYS_LIST_SUCCESS,
    categories
  };
};

const getCategoryListFail = error => {
  return {
    type: actionTypes.GET_CATEGORYS_LIST_FAIL,
    error: error
  };
};

export const getCategories = token => {
  return dispatch => {
    dispatch(getCategoryListStart());
    axios.defaults.headers = {
      "Content-Type": "application/json",
      Authorization: `Token ${token}`
    };
    axios
      .get("http://127.0.0.1:8000/grocery/category/")
      .then(res => {
        console.log(res.data.results)
        const categories = res.data.results;
        dispatch(getCategoryListSuccess(categories));
      })
      .catch(err => {
        dispatch(getCategoryListFail());
      });
  };
};