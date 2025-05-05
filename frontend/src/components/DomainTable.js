import React from "react";
import { Table, TableHead, TableBody, TableRow, TableCell, Paper, TableContainer } from "@mui/material";

const DomainTable = ({ data }) => (
  <TableContainer component={Paper} elevation={3} sx={{ p: 2, mt: 4 }}>
    <Table sx={{ width: "100%", tableLayout: "auto" }}>
      <TableHead sx={{ backgroundColor: "#2196F3" }}>
        <TableRow>
          <TableCell sx={{ color: "white", fontWeight: "bold" }}>Domain Name</TableCell>
          <TableCell sx={{ color: "white", fontWeight: "bold" }}>Registrar</TableCell>
          <TableCell sx={{ color: "white", fontWeight: "bold" }}>Registration Date</TableCell>
          <TableCell sx={{ color: "white", fontWeight: "bold" }}>Expiration Date</TableCell>
          <TableCell sx={{ color: "white", fontWeight: "bold" }}>Estimated Domain Age</TableCell>
          <TableCell sx={{ color: "white", fontWeight: "bold" }}>Hostnames</TableCell>
        </TableRow>
      </TableHead>
      <TableBody>
        <TableRow>
          <TableCell sx={{ wordBreak: "break-word" }}>{data.domainName}</TableCell>
          <TableCell sx={{ wordBreak: "break-word" }}>{data.registrar}</TableCell>
          <TableCell sx={{ wordBreak: "break-word" }}>{data.registrationDate}</TableCell>
          <TableCell sx={{ wordBreak: "break-word" }}>{data.expirationDate}</TableCell>
          <TableCell sx={{ wordBreak: "break-word" }}>{data.estimatedDomainAge} days</TableCell>
          <TableCell sx={{ wordBreak: "break-word" }}>{data.hostnames}</TableCell>
        </TableRow>
      </TableBody>
    </Table>
  </TableContainer>
);

export default DomainTable;