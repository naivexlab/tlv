import React, { useState } from "react";
import axios from "axios";
import { Container, Typography, TextField, Select, MenuItem, Button, Box, Paper } from "@mui/material";
import DomainTable from "./components/DomainTable";
import ContactTable from "./components/ContactTable";

const App = () => {
  const [domain, setDomain] = useState("");
  const [dataType, setDataType] = useState("domain_info");
  const [response, setResponse] = useState(null);
  const [errorMessage, setErrorMessage] = useState("");

  const fetchWhoisData = async () => {
    try {
      setErrorMessage("");
      const res = await axios.get(`http://localhost:8000/search`, {
        params: { domain, data_type: dataType },
      });
      setResponse(res.data);
    } catch (err) {
      if (err.response?.data) {
        setErrorMessage(err.response.data.message || "An error occurred.");
      } else {
        setErrorMessage(`Error while fetching ${domain} info.`);
      }
      setResponse(null);
    }
  };

  return (
    <Container maxWidth="md" sx={{ mt: 5 }}>
      <Paper elevation={4} sx={{ p: 4 }}>
        <Typography variant="h4" align="center" gutterBottom color="primary">
          TLV300 WHOIS Lookup
        </Typography>

        {/* Search Inputs */}
        <Box display="flex" gap={2} alignItems="center" justifyContent="center" mb={3}>
          <TextField
            fullWidth
            label="Enter Domain"
            variant="outlined"
            value={domain}
            onChange={(e) => setDomain(e.target.value)}
          />
          <Select
            value={dataType}
            onChange={(e) => setDataType(e.target.value)}
            variant="outlined"
          >
            <MenuItem value="domain_info">Domain Info</MenuItem>
            <MenuItem value="contact_info">Contact Info</MenuItem>
          </Select>
          <Button variant="contained" color="primary" onClick={fetchWhoisData}>
            Search
          </Button>
        </Box>

        {/* Response Messages */}
        {errorMessage && <Typography color="error" align="center">{errorMessage}</Typography>}
        {response?.status === "success" && (
          <Typography color="success.main" align="center" gutterBottom>{response.message}</Typography>
        )}

        {/* Tables */}
        <Box mt={4}>
          {dataType === "domain_info" && response?.status === "success" && <DomainTable data={response.data} />}
          {dataType === "contact_info" && response?.status === "success" && <ContactTable data={response.data} />}
        </Box>
      </Paper>
    </Container>
  );
};

export default App;