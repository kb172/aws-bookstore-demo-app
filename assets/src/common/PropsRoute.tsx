/* Name: Kyle Beaumont, ID: 1505627 */
import React from "react";
import { Route } from "react-router";

//@ts-ignore
export default ({ component: C, props: cProps, ...rest }) =>
  <Route {...rest} render={props => <C {...props} {...cProps} />} />;
