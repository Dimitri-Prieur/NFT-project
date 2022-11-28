
import os
from dotenv import load_dotenv
ethers = require('ethers');
load_dotenv()

# Get Alchemy App URL
API_KEY = os.getenv("API_Token")

# Define an Alchemy Provider
provider = ethers.providers.AlchemyProvider('goerli', API_KEY)

# Get contract ABI file
contract = require("../artifacts/contracts/MyNFT.sol/MyNFT.json");

# Create a signer
privateKey = os.getenv("Private_Key")
signer = ethers.Wallet(privateKey, provider)

# Get contract ABI and address
abi = contract.abi
contractAddress = '0xA4766Ceb9E84a71D282A4CED9fB8Fe93C49b2Ff7'

# Create a contract instance
myNftContract = ethers.Contract(contractAddress, abi, signer)

# Get the NFT Metadata IPFS URL
tokenUri = "https://gateway.pinata.cloud/ipfs/QmYueiuRNmL4MiA2GwtVMm6ZagknXnSpQnB3z2gWbz36hP"
""" 
// Call mintNFT function
mintNFT = async () => {
    let nftTxn = await myNftContract.mintNFT(signer.address, tokenUri)
    await nftTxn.wait()
    console.log(`NFT Minted! Check it out at: https://goerli.etherscan.io/tx/${nftTxn.hash}`)
}

mintNFT()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    }); """

    # D'abord déployé avec npm https://docs.alchemy.com/docs/how-to-create-an-nft
    # Ensuite modifié le code ci dessus pour python pour mint et changer en web3 ethers3

    # metamask
    # opensea
    # polygon

    # Mint after in Pinata
    # JSON décrit métadata