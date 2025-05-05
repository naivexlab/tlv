import React from "react";
import { Table, TableHead, TableBody, TableRow, TableCell, Paper, TableContainer } from "@mui/material";

const ContactTable = ({ data }) => (
  <TableContainer component={Paper} elevation={3} sx={{ p: 2, mt: 4 }}>
    <Table sx={{ width: "100%", tableLayout: "auto" }}>
      <TableHead sx={{ backgroundColor: "#2196F3" }}>
        <TableRow>
          <TableCell sx={{ color: "white", fontWeight: "bold" }}>Registrant Name</TableCell>
          <TableCell sx={{ color: "white", fontWeight: "bold" }}>Technical Contact</TableCell>
          <TableCell sx={{ color: "white", fontWeight: "bold" }}>Administrative Contact</TableCell>
          <TableCell sx={{ color: "white", fontWeight: "bold" }}>Contact Email</TableCell>
        </TableRow>
      </TableHead>
      <TableBody>
        <TableRow>
          <TableCell sx={{ wordBreak: "break-word" }}>{data.registrantName}</TableCell>
          <TableCell sx={{ wordBreak: "break-word" }}>{data.technicalContactName}</TableCell>
          <TableCell sx={{ wordBreak: "break-word" }}>{data.administrativeContactName}</TableCell>
          <TableCell sx={{ wordBreak: "break-word" }}>{data.contactEmail}</TableCell>
        </TableRow>
      </TableBody>
    </Table>
  </TableContainer>
);

export default ContactTable;