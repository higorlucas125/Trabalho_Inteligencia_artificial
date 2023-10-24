import React from "react";
import {
  LineChart,
  Line,
  BarChart,
  Bar,
  Rectangle,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";

import {
  BsFillArchiveFill,
  BsFillGrid3X3GapFill,
  BsPeopleFill,
  BsFillGearFill,
} from "react-icons/bs";

import './index.css'

const data = [
  {
    name: "Etapa 8",
    miniMax: 295137,
    alfaBeta: 18168,
    amt: 300000,
  },
  {
    name: "Etapa 7",
    miniMax: 31996,
    alfaBeta: 2525,
    amt: 300000,
  },
  {
    name: "Etapa 6",
    miniMax: 3871,
    alfaBeta: 904,
    amt: 300000,
  },
  {
    name: "Etapa 5",
    miniMax: 477,
    alfaBeta: 137,
    amt: 300000,
  },
  {
    name: "Etapa 4",
    miniMax: 103,
    alfaBeta: 55,
    amt: 300000,
  },
  {
    name: "Etapa 3",
    miniMax: 25,
    alfaBeta: 19,
    amt: 300000,
  },
  {
    name: "Etapa 2",
    miniMax: 7,
    alfaBeta: 7,
    amt: 300000,
  },
  {
    name: "Etapa 1",
    miniMax: 2,
    alfaBeta: 2,
    amt: 300000,
  },
  {
    name: "Etapa 0",
    miniMax: 0,
    alfaBeta: 0,
    amt: 300000,
  },
];

const Home = ({produtcs,categories,customers,alerts}) => {

  return (
    <main className="main-container">
      <div className="main-title">
        <h3>DASHBOAR</h3>
      </div>
      <div className="main-cards">
        <div className="card">
          <div className="card-inner">
            <h3>PRODUCTS</h3>
            <BsFillArchiveFill className="card_icon" />
          </div>
          <h1>{produtcs}</h1>
        </div>

        <div className="card">
          <div className="card-inner">
            <h3>CATEGORIES</h3>
            <BsFillGrid3X3GapFill className="card_icon" />
          </div>
          <h1>{categories}</h1>
        </div>

        <div className="card">
          <div className="card-inner">
            <h3>CUSTOMERS</h3>
            <BsPeopleFill className="card_icon" />
          </div>
          <h1>{customers}</h1>
        </div>

        <div className="card">
          <div className="card-inner">
            <h3>ALERTS</h3>
            <BsFillGearFill className="card_icon" />
          </div>
          <h1>{alerts}</h1>
        </div>
      </div>
      <div className="charts">
        <ResponsiveContainer width="100%" height="100%">
          <BarChart
            width={500}
            height={300}
            data={data}
            margin={{
              top: 5,
              right: 30,
              left: 20,
              bottom: 5,
            }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Bar
              dataKey="alfaBeta"
              fill="#8884d8"
              activeBar={<Rectangle fill="pink" stroke="blue" />}
            />
            <Bar
              dataKey="miniMax"
              fill="#82ca9d"
              activeBar={<Rectangle fill="gold" stroke="purple" />}
            />
          </BarChart>
        </ResponsiveContainer>

        <ResponsiveContainer width="100%" height="100%">
          <LineChart
            width={500}
            height={300}
            data={data}
            margin={{
              top: 5,
              right: 30,
              left: 20,
              bottom: 5,
            }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Line
              type="monotone"
              dataKey="alfaBeta"
              stroke="#8884d8"
              activeDot={{ r: 8 }}
            />
            <Line type="monotone" dataKey="miniMax" stroke="#82ca9d" />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </main>
  );
};

export default Home;
