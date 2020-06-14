import React from "react";
import { Route } from "react-router-dom";
import Hoc from "./hoc/hoc";

import Login from "./containers/Login";
import Signup from "./containers/Signup";
import Profile from "./containers/Profile";
import ProductList from "./containers/ProductList";
import ProductDetail from "./containers/ProductDetail";
import ProductCreate from "./containers/ProductCreate";
import OrderDetail from "./containers/OrderDetail";
import OrderList from "./containers/OrderList";
import CustomLayout from "./containers/layout";
import ChangePassword from "./containers/ChangePassword";

const BaseRouter = () => (
  <Hoc>
    <Route exact path="/login/" component={Login} />
    <Route exact path="/signup/" component={Signup} />
      <CustomLayout>
        <Route exact path="/" component={Profile} />
        <Route exact path="/profile/:id" component={Profile} />
        <Route exact path="/product/" component={ProductList} />
        <Route exact path="/product/detail" component={ProductDetail} />
        <Route exact path="/product/create/" component={ProductCreate} />
        <Route exact path="/order/" component={OrderList} />
        <Route exact path="/order/:id" component={OrderDetail} />
        <Route exact path="/change-password/" component={ChangePassword} />
      </CustomLayout>
  </Hoc>
);

export default BaseRouter;
