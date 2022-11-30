// We require the Hardhat Runtime Environment explicitly here. This is optional
// but useful for running the script in a standalone fashion through `node <script>`.
//
// You can also run a script with `npx hardhat run <script>`. If you do that, Hardhat
// will compile your contracts, add the Hardhat Runtime Environment's members to the
// global scope, and execute the script.
const hre = require("hardhat");

async function main() {

  const TiketEvent = await hre.ethers.getContractFactory("tiketEvent");
  const tiketEvent = await TiketEvent.attach("0x867fCDD5F86b01E195283637dB0D97c3D7189da4");

  await tiketEvent.mintNFT("0xC841962098B5592A415493992cd7F521347632f7", "https://gateway.pinata.cloud/ipfs/QmWWfgT12dRhtXDmpD2QMM7vn9aYw2nfMVXQoS3L5ZMPnJ");

  console.log(
    ` deployed to ${tiketEvent.address}`
  );
}

// We recommend this pattern to be able to use async/await everywhere
// and properly handle errors.
main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});