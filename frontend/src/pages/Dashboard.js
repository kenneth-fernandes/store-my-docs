import React, { useContext } from "react";
import { useNavigate } from "react-router-dom";
import { AuthContext } from "../context/AuthContext";
import { toast } from "react-toastify";

const Dashboard = () => {
    const { setAuth } = useContext(AuthContext);
    const navigate = useNavigate();

    const handleLogout = () => {
        setAuth(null);
        localStorage.removeItem("token");
        toast.success("Logged out successfully!");
        navigate("/");
    };

    return (
      <div className="dashboard-container">
        <h2>Welcome to Store My Docs</h2>
        <p>You are logged in successfully.</p>
        <button onClick={handleLogout} className="logout-btn">
          Logout
        </button>
      </div>
    );
};

export default Dashboard;