require("@nomicfoundation/hardhat-toolbox");


module.exports = {
  solidity: "0.8.17",
  networks: {
    mumbai: {
      url: "https://polygon-mumbai.g.alchemy.com/v2/xPACxJYzW3ovyVZS_NMuOHO-BZaKcF2d",
      accounts:["061b19c506fad653454da231e21f35a4432bdcf5ef2aab7097e0fa9e29d3ed49"],
    },
  },
};
